from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
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


class GetTrucksAvailabilityDetailsView(generics.ListAPIView):
    serializer_class = GetTruckAvailabilitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        from_location = self.request.query_params.get('from_location')
        to_location = self.request.query_params.get('to_location')
        total_weight = self.request.query_params.get('total_weight')
        queryset = TruckAvailability.objects.all()
        if from_location is not None:
            queryset = queryset.filter(source_location=from_location, destination=to_location, status=True,
                                       truck_type__truck_total_weight__lte=total_weight).order_by('truck_type__truck_type')
        return queryset
