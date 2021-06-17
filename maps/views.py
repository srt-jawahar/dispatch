from .serializers import GetFreightOrderStatusSerializers
from rest_framework import generics, permissions
from freight_order.models import FreightOrders


# Create your views here.
class FreightOrderStatusView(generics.RetrieveAPIView):
    serializer_class = GetFreightOrderStatusSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        ASSIGNED = 'Assigned'
        freight_order_number = self.request.query_params.get('freight_order_number')
        queryset = FreightOrders.objects.all()
        if freight_order_number is not None:
            queryset = queryset.filter(freight_order_no=freight_order_number, freight_status=ASSIGNED, )
        return queryset
