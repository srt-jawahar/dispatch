from django.db.models import Max, Min, Q
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins, status, permissions
from rest_framework import generics
from .serializers import FreightOrdersSerializer, FreightTruckAssignSerializer, FreightTruckConfirmSerializer, \
    FreightOrdersGetSerializer
from .models import FreightOrders, FreightTruckAssignments
from rest_framework.response import Response
from truckmanagement.models import TruckAvailability, TruckDetails


# Starting of freight order creation
class FreightView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FreightOrdersSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # get the data which sent from UI
        reqdata = request.data
        serializer = self.get_serializer(data=reqdata, many=True)
        serializer.is_valid(raise_exception=True)

        # declare the dictionary to calculate total weight and total volume
        total_weight = {}
        total_volume = {}
        from_location = {}
        destination = {}
        final_suggested_truck_type = ''
        final_no_of_trucks = 0
        user_name = request.user.username

        # iterate the data to calculate total weight and total volume
        for deli in reqdata:
            del_no = deli.get('delivery_no', None)
            weight = deli.get('total_weight', None)
            volume = deli.get('total_volume', None)
            region = deli.get('destination', None)
            from_loc = deli.get('from_location', None)

            try:
                initial_value_weight = total_weight[del_no]
                initial_value_vol = total_volume[del_no]
            except KeyError:
                initial_value_weight = 0
                initial_value_vol = 0

            total_weight[del_no] = initial_value_weight + weight
            total_volume[del_no] = initial_value_vol + volume

            destination[del_no] = region
            from_location[del_no] = from_loc

        # get max freight order no from DB to create the new freight orders
        freight_order_no_max = ''
        next_freight_number = FreightOrders.objects.aggregate(freight_order_no_max=Max('freight_order_no'))

        # Max value returned as dictionary type. So that try to get that max value and defaulted to 10000 if None
        for next_no in next_freight_number:
            if next_freight_number[next_no] is None:
                freight_order_no_max = '10000'
            else:
                freight_order_no_max = next_freight_number[next_no]

        # iterate the grouped delivery numbers to create freight orders
        for deli_no in total_weight:
            converted_no = int(freight_order_no_max) + 1
            freight_order_no_max = str(converted_no)
            freight_order = FreightOrders()
            freight_order.freight_order_no = freight_order_no_max
            freight_order.delivery_no = deli_no
            freight_order.total_weight = total_weight[deli_no]
            freight_order.total_volume = total_volume[deli_no]
            freight_order.from_location = from_location[deli_no]
            freight_order.destination = destination[deli_no]

            # suggested truck logic
            '''avail_truck_ids = TruckAvailability.objects.filter(source_location=freight_order.from_location,
                                                               destination=freight_order.destination,
                                                               no_of_trucks__gte=1).values('truck_type_id')'''
            avail_truck_ids = TruckAvailability.objects.filter(source_location=freight_order.from_location,
                                                               destination=freight_order.destination).values(
                'truck_type_id')
            if not avail_truck_ids:
                return Response({"message": "No available trucks for the delivery no " + deli_no},
                                status=status.HTTP_400_BAD_REQUEST)

            min_truck_value = TruckDetails.objects.filter(id__in=avail_truck_ids,
                                                          truck_total_weight__gte=freight_order.total_weight).aggregate(
                truck_total_weight=Min('truck_total_weight'))
            truck_count = 2
            for truck in min_truck_value:
                if min_truck_value[truck] is None:
                    next_min_truck_value = TruckDetails.objects.filter(id__in=avail_truck_ids).aggregate(
                        truck_total_weight=Min('truck_total_weight'))
                    for tru in next_min_truck_value:
                        second_value = next_min_truck_value[tru]
                        for i in range(2, 100, 1):
                            if second_value * i >= freight_order.total_weight:
                                truck_count = i
                                final_truck_id = TruckDetails.objects.filter(id__in=avail_truck_ids,
                                                                             truck_total_weight=next_min_truck_value[
                                                                                 tru]).values('id')
                                final_avail_truck = TruckAvailability.objects.filter(truck_type_id__in=final_truck_id)
                                if not final_avail_truck:
                                    return Response({"message": "No available trucks for the delivery no " + deli_no},
                                                    status=status.HTTP_400_BAD_REQUEST)
                                for final_truck in final_avail_truck:
                                    final_suggested_truck_type = final_truck.truck_type
                                    final_no_of_trucks = truck_count
                                break
                else:
                    final_truck_id = TruckDetails.objects.filter(id__in=avail_truck_ids,
                                                                 truck_total_weight=min_truck_value[truck]).values('id')
                    final_avail_truck = TruckAvailability.objects.filter(truck_type_id__in=final_truck_id)
                    truck_count = 1
                    if not final_avail_truck:
                        return Response({"message": "No available trucks for the delivery no " + deli_no},
                                        status=status.HTTP_400_BAD_REQUEST)
                    for final_truck in final_avail_truck:
                        final_suggested_truck_type = final_truck.truck_type
                        final_no_of_trucks = truck_count

            freight_order.created_by = user_name
            freight_order.updated_by = user_name
            freight_order.save()
            # Suggested Truck assignments
            freight_truck_assign = FreightTruckAssignments()
            freight_truck_assign.freight_order = freight_order
            freight_truck_assign.freight_order_no = freight_order.freight_order_no
            freight_truck_assign.suggested_truck_type = final_suggested_truck_type
            freight_truck_assign.no_of_trucks = final_no_of_trucks
            freight_truck_assign.created_by = user_name
            freight_truck_assign.updated_by = user_name
            freight_truck_assign.save()

        return Response(status=status.HTTP_201_CREATED)


# Ending of freight order creation


# Starting of truck confirmation to the freight orders
class FreightTruckConfirmView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FreightTruckConfirmSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request):
        reqdata = request.data
        serializer = self.get_serializer(data=reqdata, many=True)
        serializer.is_valid(raise_exception=True)

        user_name = request.user.username

        for freight_data in reqdata:
            freight_order_no = freight_data.get('freight_order_no', None)
            freight_order = FreightOrders.objects.filter(freight_order_no=freight_order_no)
            if not freight_order:
                return Response({"message": "No fright order : " + freight_order_no},
                                status=status.HTTP_400_BAD_REQUEST)
            for order in freight_order:
                if FreightOrders.CONFIRMED == order.freight_status:
                    return Response({"message": "Fright order:" + freight_order_no + " already confirmed"},
                                    status=status.HTTP_400_BAD_REQUEST)
                if FreightOrders.ASSIGNED == order.freight_status:
                    return Response({"message": "Fright order:" + freight_order_no + " already assigned"},
                                    status=status.HTTP_400_BAD_REQUEST)
                # Get the details from truck assignment and update the confirmation details
                fright_assignments = FreightTruckAssignments.objects.filter(freight_order_no=freight_order_no)
                for fright_assign in fright_assignments:
                    fright_assign.suggested_truck_type = freight_data.get('suggested_truck_type', None)
                    fright_assign.no_of_trucks = freight_data.get('no_of_trucks', None)
                    fright_assign.updated_by = user_name
                    fright_assign.save()

                # Update status
                order.freight_status = FreightOrders.CONFIRMED
                order.updated_by = user_name
                order.save()

                return Response(status=status.HTTP_200_OK)


# Ending of truck confirmation to the freight orders


# To get all freight order list
class GetAllFreightView(generics.ListAPIView):
    serializer_class = FreightOrdersGetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return FreightOrders.objects.all()


# To get confirmed freight order list to assign truck
class GetConfirmedFreightView(generics.ListAPIView):
    serializer_class = FreightOrdersGetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return FreightOrders.objects.filter(
            Q(freight_status=FreightOrders.CONFIRMED) | Q(freight_status=FreightOrders.ASSIGNED))


# Starting of truck assignment to the freight orders
class FreightTruckAssignView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request):
        reqdata = request.data
        # serializer = self.get_serializer(data=reqdata, many=True)
        # serializer.is_valid(raise_exception=True)

        user_name = request.user.username

        for freight_data in reqdata:
            freight_order_no = freight_data.get('freight_order_no', None)
            freight_order = FreightOrders.objects.filter(freight_order_no=freight_order_no)
            if not freight_order:
                return Response({"message": "No fright order : " + freight_order_no},
                                status=status.HTTP_400_BAD_REQUEST)
            for order in freight_order:
                if FreightOrders.ASSIGNED == order.freight_status:
                    return Response({"message": "Fright order:" + freight_order_no + " already assigned"},
                                    status=status.HTTP_400_BAD_REQUEST)
                if FreightOrders.SUGGESTED == order.freight_status:
                    return Response({"message": "Fright order:" + freight_order_no + " should be confirmed"},
                                    status=status.HTTP_400_BAD_REQUEST)
                # Get the details from truck assignment and update the confirmation details
                FreightTruckAssignments.objects.filter(freight_order_no=freight_order_no).delete()
                if not freight_data.get('truck_types'):
                    return Response({"message": "truck_types mandatory"},
                                    status=status.HTTP_400_BAD_REQUEST)
                for fright_assign in freight_data.get('truck_types', None):
                    if not fright_assign.get('transportor_name'):
                        return Response({"message": "Transporter name mandatory"},
                                        status=status.HTTP_400_BAD_REQUEST)
                    new_freight_assign = FreightTruckAssignments()
                    new_freight_assign.freight_order = order
                    new_freight_assign.freight_order_no = order.freight_order_no
                    new_freight_assign.suggested_truck_type = fright_assign.get('suggested_truck_type', None)
                    new_freight_assign.no_of_trucks = fright_assign.get('no_of_trucks', None)
                    new_freight_assign.transportor_name = fright_assign.get('transportor_name', None)
                    new_freight_assign.created_by = user_name
                    new_freight_assign.updated_by = user_name
                    # update the reserved truck
                    truck_type = TruckDetails.objects.filter(truck_type=new_freight_assign.suggested_truck_type).first()
                    truck_availability = TruckAvailability.objects.filter(
                        transportor_name=new_freight_assign.transportor_name,
                        truck_type=truck_type).first()
                    truck_availability.no_of_trucks_reserved = truck_availability.no_of_trucks_reserved + \
                                                               new_freight_assign.no_of_trucks
                    truck_availability.save()
                    new_freight_assign.save()

                # Update status
                order.freight_status = FreightOrders.ASSIGNED
                if freight_data.get('remarks'):
                    order.remarks = freight_data.get('remarks')
                order.updated_by = user_name
                order.save()

                return Response(status=status.HTTP_200_OK)


# Ending of truck assignment to the freight orders


# To get assigned freight order list to view
class GetAssignedFreightView(generics.ListAPIView):
    serializer_class = FreightOrdersGetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return FreightOrders.objects.filter(freight_status=FreightOrders.ASSIGNED)
