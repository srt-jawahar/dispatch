from rest_framework import serializers
from .models import Plants, Customers
from django.contrib.auth.models import User

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
