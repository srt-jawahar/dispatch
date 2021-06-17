from freight_order.models import FreightOrders
from rest_framework import serializers


class GetFreightOrderStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = FreightOrders
        fields = '__all__'
