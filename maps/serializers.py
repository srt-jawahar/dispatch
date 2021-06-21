from freight_order.models import FreightOrders
from rest_framework import serializers


class GetFreightOrderStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = FreightOrders
        fields = '__all__'


class UpdateFreightOrderStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = FreightOrders
        fields = ['remarks', 'truck_number', 'truck_driver_details', 'truck_current_pos', 'truck_status']
