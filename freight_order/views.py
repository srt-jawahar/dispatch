from django.db.models import Max
from django.shortcuts import render
from rest_framework import mixins, status, permissions
from rest_framework import generics
from .serializers import FreightOrdersSerializer
from .models import FreightOrders
from rest_framework.response import Response

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

        # Max value returned as dictionary type. So that try to get that max value and defaulted to 10000 if Key error
        try:
            freight_order_no_max = next_freight_number[freight_order_no_max]
        except KeyError:
            freight_order_no_max = '10000'

        # iterate the grouped delivery numbers to create freight orders
        for deli_no in total_weight:
            converted_no = int(freight_order_no_max) + 1
            freight_order_no_max = str(converted_no)
            freight_order = FreightOrders()
            freight_order.freight_order_no = freight_order_no_max
            freight_order.delivery_no = deli_no
            freight_order.total_weight = total_weight[deli_no]
            freight_order.total_volume = total_volume[deli_no]
            freight_order.from_location = 'from'
            freight_order.destination = destination[deli_no]
            freight_order.suggested_truck_type = 'TruckA'
            freight_order.no_of_trucks = 2
            freight_order.save()

        return Response(status=status.HTTP_201_CREATED)
