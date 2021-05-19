from django.shortcuts import render
from rest_framework import mixins, status, permissions
from rest_framework import generics
from .serializers import PlantSerializer, CustomerSerializer, DeliveryDetailsSerializer
from .models import Plants, Customers, DeliveryDetails
from rest_framework.response import Response


# Starting of plant view
class PlantFromSAPView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PlantSerializer
    queryset = Plants.objects.all()
    lookup_field = 'PLANT'

    def post(self, request, PLANT=None):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request, PLANT=None):
        return self.update(request, PLANT)

    def delete(self, request, PLANT=None):
        return self.destroy(request, PLANT)


class PlantListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PlantSerializer
    queryset = Plants.objects.all()
    lookup_field = 'PLANT'
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, PLANT=None):

        if PLANT:
            return self.retrieve(request)
        else:
            return self.list(request)
# End of plant view


# Starting of customer view
class CustomerFromSAPView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.all()
    lookup_field = 'CUST_ID'

    def post(self, request, CUST_ID=None):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request, CUST_ID=None):
        return self.update(request, CUST_ID)

    def delete(self, request, CUST_ID=None):
        return self.destroy(request, CUST_ID)



class CustomerListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.all()
    lookup_field = 'CUST_ID'
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, CUST_ID=None):

        if CUST_ID:
            return self.retrieve(request)
        else:
            return self.list(request)
# End of customer view


# Starting of delivery view
class DeliveryDetailsFromSAPView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DeliveryDetailsSerializer
    queryset = DeliveryDetails.objects.all()
    lookup_field = 'CUST_ID'

    def post(self, request, CUST_ID=None):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request, CUST_ID=None):
        return self.update(request, CUST_ID)

    def delete(self, request, CUST_ID=None):
        return self.destroy(request, CUST_ID)



class DeliveryDetailsListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = DeliveryDetailsSerializer
    queryset = DeliveryDetails.objects.all()
    lookup_field = 'CUST_ID'
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, CUST_ID=None):

        if CUST_ID:
            return self.retrieve(request)
        else:
            return self.list(request)
# End of delivery view
