from django.urls import path
from .views import FreightView, FreightTruckAssignView


urlpatterns = [
   # freight urls
   path('freightOrder/', FreightView.as_view()),
   path('freightTruckAssign/', FreightTruckAssignView.as_view()),
]
