from django.urls import path

from .views import TruckListCreateView, TruckUpdateRetrieveDeleteView, TruckAvailabilityListCreateView, TruckAvailibilityUpdateRetrieveDeleteView,\
    GetTruckAvailability

urlpatterns = [
    path('trucks/', TruckListCreateView.as_view(), name='trucks'),
    path('truck/<int:pk>', TruckUpdateRetrieveDeleteView.as_view(), name='truck'),
    path('trucks_availability/', TruckAvailabilityListCreateView.as_view(), name='truck-availability'),
    path('trucks_availability/<int:pk>', TruckAvailibilityUpdateRetrieveDeleteView.as_view(), name='truck-availability'),
    path('trucks_availability_with_details/', GetTruckAvailability.as_view(), name='truck-availability-with-details')
]
