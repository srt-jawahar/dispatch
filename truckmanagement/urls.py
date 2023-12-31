from django.urls import path

from .views import TruckListCreateView, TruckUpdateRetrieveDeleteView, TruckAvailabilityListCreateView, TruckAvailibilityUpdateRetrieveDeleteView,\
    GetTruckAvailability, GetTrucksAvailabilityDetailsView, GetTrucksAvailabilityDetailsOfTruckTypeView

urlpatterns = [
    path('trucks/', TruckListCreateView.as_view(), name='trucks'),
    path('truck/<int:pk>', TruckUpdateRetrieveDeleteView.as_view(), name='truck'),
    path('trucks_availability/', TruckAvailabilityListCreateView.as_view(), name='truck-availability'),
    path('trucks_availability/<int:pk>', TruckAvailibilityUpdateRetrieveDeleteView.as_view(), name='truck-availability'),
    path('trucks_availability_with_details/', GetTruckAvailability.as_view(), name='truck-availability-with-details'),
    path('get_all_truck_availability_list/', GetTrucksAvailabilityDetailsView.as_view(), name='truck_availability_status'),
    path('get_truck_availability_list/', GetTrucksAvailabilityDetailsOfTruckTypeView.as_view(), name='truck_availability_status')
]
