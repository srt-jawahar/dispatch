from django.urls import path

from .views import TruckListCreateView, TruckUpdateRetrieveDeleteView, TruckAvailabilityListCreateView, TruckAvailibilityUpdateRetrieveDeleteView

urlpatterns = [
    path('trucks/', TruckListCreateView.as_view(), name='trucks'),
    path('truck/<int:pk>', TruckUpdateRetrieveDeleteView.as_view(), name='truck'),
    path('trucks_availibility/', TruckAvailabilityListCreateView.as_view(), name='truck-availability'),
    path('trucks_availibility/<int:pk>', TruckAvailibilityUpdateRetrieveDeleteView.as_view(), name='truck-availability'),
]
