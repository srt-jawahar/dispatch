from django.urls import path
from .views import FreightView, FreightTruckAssignView, FreightTruckConfirmView, GetAllFreightView


urlpatterns = [
   # freight urls
   path('freightOrder/', FreightView.as_view()),  # to create the freight order
   path('freightTruckAssign/', FreightTruckAssignView.as_view()),
   path('freightTruckConfirm/', FreightTruckConfirmView.as_view()),  # to confirm the truck type
   path('getFreightList/', GetAllFreightView.as_view()),  # to get list of freight orders
]
