from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TruckSerializer
from .models import TruckDetails


class TruckListCreateView(generics.ListCreateAPIView):
    queryset = TruckDetails.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]


class TruckUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TruckDetails.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]
