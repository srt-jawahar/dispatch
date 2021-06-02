from rest_framework import serializers
from .models import FreightOrders, FreightTruckAssignments


class FreightOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightOrders
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'freight_order_no', 'from_location',
                            'delivery_id', 'transportor_name')


class FreightTruckAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightOrders
        fields = '__all__'
        read_only_fields = ('delivery_no', 'created_by', 'updated_by',  'from_location', 'delivery_id',
                            'total_volume', 'total_weight', 'destination')


class FreightTruckConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightTruckAssignments
        fields = '__all__'
        read_only_fields = ('freight_order', 'created_by', 'updated_by', 'transportor_name')


class FreightTruckAssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightTruckAssignments
        fields = '__all__'


class FreightOrdersGetSerializer(serializers.ModelSerializer):
    freighttruckassignments_set = FreightTruckAssignmentsSerializer(many=True)
    class Meta:
        model = FreightOrders
        fields = '__all__'
