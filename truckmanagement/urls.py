from django.urls import path

from .views import TruckListCreateView, TruckUpdateRetrieveDeleteView

urlpatterns = [
    path('trucks/', TruckListCreateView.as_view(), name='trucks'),
    path('truck/<int:pk>', TruckUpdateRetrieveDeleteView.as_view(), name='truck'),
]
