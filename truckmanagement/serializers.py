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
    truck_master = TruckSerializer(many=False, read_only=True)

    class Meta:
        model = TruckAvailability
        fields = ['truck_master', 'source_location', 'destination', 'no_of_trucks', 'availability', 'created_at', 'remarks', 'no_of_trucks_reserved']