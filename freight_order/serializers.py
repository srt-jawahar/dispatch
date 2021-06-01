from rest_framework import serializers
from .models import FreightOrders


class FreightOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightOrders
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'freight_order_no', 'from_location', 'suggested_truck_type',
                              'no_of_trucks', 'delivery_id', 'transportor_name')


class FreightTruckAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightOrders
        fields = '__all__'
        read_only_fields = ('delivery_no', 'created_by', 'updated_by', 'freight_order_no', 'from_location', 'delivery_id',
                            'total_volume', 'total_weight', 'destination')