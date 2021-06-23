from django.urls import path
from .views import FreightView, FreightTruckAssignView, FreightTruckConfirmView, GetAllFreightView,\
                   GetConfirmedFreightView, GetAssignedFreightView, CreateCarrierInvoice, GetReceiptInformation


urlpatterns = [
   # freight urls
   path('freightOrder/', FreightView.as_view()),  # to create the freight order
   path('freightTruckAssign/', FreightTruckAssignView.as_view()),
   path('freightTruckConfirm/', FreightTruckConfirmView.as_view()),  # to confirm the truck type
   path('getFreightList/', GetAllFreightView.as_view()),  # to get list of freight orders
   path('getConfirmedFreightList/', GetConfirmedFreightView.as_view()),  # to get list of confirmed freight orders
   path('getAssignedFreightList/', GetAssignedFreightView.as_view()),  # to get list of assigned freight orders
   path('updateFreightOrderDetails/<int:pk>/', CreateCarrierInvoice.as_view()),  # to create carrier invoice
   path('getReceiptDetails/<int:pk>/', GetReceiptInformation.as_view()),  # to create carrier invoice
]
