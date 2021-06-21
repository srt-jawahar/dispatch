from .serializers import GetFreightOrderStatusSerializers, UpdateFreightOrderStatusSerializers
from rest_framework import viewsets,  generics
from freight_order.models import FreightOrders


# Get particular freight order
class FreightOrderStatusView(viewsets.ModelViewSet):
    serializer_class = GetFreightOrderStatusSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        ASSIGNED = 'Assigned'
        freight_order_number = self.request.query_params.get('freight_order_no')
        queryset = FreightOrders.objects.all()
        if freight_order_number is not None:
            queryset = queryset.filter(freight_order_no=freight_order_number, freight_status=ASSIGNED, )
        return queryset


# Patch Particular freight order
class FreightOrderUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateFreightOrderStatusSerializers
