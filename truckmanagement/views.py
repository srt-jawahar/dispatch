from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TruckSerializer, TruckAvailabilitySerializer, GetTruckAvailabilitySerializer
from .models import TruckDetails, TruckAvailability


class TruckListCreateView(generics.ListCreateAPIView):
    queryset = TruckDetails.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]


class TruckUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TruckDetails.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]


class TruckAvailabilityListCreateView(generics.ListCreateAPIView):
    queryset = TruckAvailability.objects.all()
    serializer_class = TruckAvailabilitySerializer
    permission_classes = [IsAuthenticated]


class TruckAvailibilityUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TruckAvailability.objects.all()
    serializer_class = TruckAvailabilitySerializer
    permission_classes = [IsAuthenticated]


class GetTruckAvailability(generics.ListAPIView):
    queryset = TruckAvailability.objects.all()
    serializer_class = GetTruckAvailabilitySerializer
    permission_classes = [IsAuthenticated]