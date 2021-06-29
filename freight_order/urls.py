from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import FreightView, FreightTruckAssignView, FreightTruckConfirmView, GetAllFreightView, \
    GetConfirmedFreightView, GetAssignedFreightView, CreateCarrierInvoice, GetReceiptInformation, \
    UploadCarrierInvoiceView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'file', UploadCarrierInvoiceView, basename='document_details')

urlpatterns = [
    # freight urls
    path('freightOrder/', FreightView.as_view()),  # to create the freight order
    path('freightTruckAssign/', FreightTruckAssignView.as_view()),
    path('freightTruckConfirm/', FreightTruckConfirmView.as_view()),  # to confirm the truck type
    path('getFreightList/', GetAllFreightView.as_view()),  # to get list of freight orders
    path('getConfirmedFreightList/', GetConfirmedFreightView.as_view()),  # to get list of confirmed freight orders
    path('getAssignedFreightList/', GetAssignedFreightView.as_view()),  # to get list of assigned freight orders
    path('updateFreightOrderDetails/<int:pk>/', CreateCarrierInvoice.as_view()),  # to create carrier invoice
    path('getReceiptOrCarrierInvoiceDetails/', GetReceiptInformation.as_view()),  # to get carrier invoice
    path('uploadCarrierInvoice/', include(router.urls)),  # to get carrier invoice
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)