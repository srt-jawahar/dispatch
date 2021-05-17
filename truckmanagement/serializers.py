from rest_framework import serializers
from .models import TruckDetails


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckDetails
        fields = '__all__'
