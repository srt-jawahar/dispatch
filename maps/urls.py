from django.urls import path
from .views import FreightOrderStatusView, FreightOrderUpdateView

urlpatterns = [
    path("maps/<int:pk>/", FreightOrderStatusView.as_view({'get': 'retrieve'}), name="get_freight_order_details"),
    path("maps_update/<int:pk>/", FreightOrderUpdateView.as_view(), name="update_freight_order_details"),
]
