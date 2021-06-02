from rest_framework import serializers
from .models import TruckDetails, TruckAvailability


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckDetails
        fields = '__all__'


class TruckAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckAvailability
        fields = '__all__'


class GetTruckAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckAvailability
        fields = "__all__"
        depth = 1
