from django.db.models import Max, Min
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins, status, permissions
from rest_framework import generics
from .serializers import FreightOrdersSerializer, FreightTruckAssignSerializer
from .models import FreightOrders
from rest_framework.response import Response
from truckmanagement.models import TruckAvailability, TruckDetails


# Starting of freight order creation
class FreightView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FreightOrdersSerializer
    queryset = FreightOrders.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return self.list(request)

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

        # iterate the data to calculate total weight and total volume
        for deli in reqdata:
            del_no = deli.get('delivery_no', None)
            weight = deli.get('total_weight', None)
            volume = deli.get('total_volume', None)
            region = deli.get('destination', None)

            try:
                initial_value_weight = total_weight[del_no]
                initial_value_vol = total_volume[del_no]
            except KeyError:
                initial_value_weight = 0
                initial_value_vol = 0

            total_weight[del_no] = initial_value_weight + weight
            total_volume[del_no] = initial_value_vol + volume

            destination[del_no] = region

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
            freight_order.from_location = 'chennai'
            freight_order.destination = destination[deli_no]

            # suggested truck logic
            avail_truck_ids = TruckAvailability.objects.filter(source_location=freight_order.from_location,
                                                               destination=freight_order.destination,
                                                               no_of_trucks__gte=1).values('truck_type_id')
            if not avail_truck_ids:
                return Response({"message": "No available trucks"}, status=status.HTTP_400_BAD_REQUEST)

            min_truck_value = TruckDetails.objects.filter(id__in=avail_truck_ids,
                                                          truck_max_capacity__gte=freight_order.total_weight).aggregate(
                truck_max_capacity=Min('truck_max_capacity'))
            truck_count = 2
            for truck in min_truck_value:
                if min_truck_value[truck] is None:
                    next_min_truck_value = TruckDetails.objects.filter(id__in=avail_truck_ids).aggregate(
                        truck_max_capacity=Min('truck_max_capacity'))
                    for tru in next_min_truck_value:
                        second_value = next_min_truck_value[tru]
                        for i in range(2, 10, 1):
                            if second_value * i >= freight_order.total_weight:
                                truck_count = i
                                final_truck_id = TruckDetails.objects.filter(id__in=avail_truck_ids,
                                                                             truck_max_capacity=next_min_truck_value[
                                                                                 tru]).values('id')
                                final_avail_truck = TruckAvailability.objects.filter(truck_type_id__in=final_truck_id)
                                for final_truck in final_avail_truck:
                                    freight_order.suggested_truck_type = final_truck.truck_type
                                    freight_order.no_of_trucks = truck_count
                                break
                else:
                    final_truck_id = TruckDetails.objects.filter(id__in=avail_truck_ids, truck_max_capacity=min_truck_value[truck]).values('id')
                    final_avail_truck = TruckAvailability.objects.filter(truck_type_id__in=final_truck_id)
                    truck_count = 1
                    for final_truck in final_avail_truck:
                        freight_order.suggested_truck_type = final_truck.truck_type
                        freight_order.no_of_trucks = truck_count

            freight_order.created_by = request.user.username
            freight_order.updated_by = request.user.username
            freight_order.save()

        return Response(status=status.HTTP_201_CREATED)
# Ending of freight order creation


# Starting of truck assignment to the freight orders
class FreightTruckAssignView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FreightTruckAssignSerializer
    queryset = FreightOrders.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request):
        reqdata = request.data
        serializer = self.get_serializer(data=reqdata, many=True)
        serializer.is_valid(raise_exception=True)

        for freight_data in reqdata:
            freight_order_no = freight_data.get('freight_order_no', None)
            freight_order = FreightOrders.objects.filter(freight_order_no=freight_order_no)
            for order in freight_order:
                order.suggested_truck_type = freight_data.get('suggested_truck_type', None)
                order.no_of_trucks = freight_data.get('no_of_trucks', None)
                order.truck_status = 'Confirmed'
                order.save()

                return Response(status=status.HTTP_200_OK)
# Ending of truck assignment to the freight orders
