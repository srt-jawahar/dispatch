from django.urls import path
from .views import FreightOrderStatusView

urlpatterns = [
    path("maps/", FreightOrderStatusView.as_view(), name="get_freight_order_details"),
]
