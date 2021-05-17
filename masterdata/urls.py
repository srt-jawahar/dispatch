from django.urls import path
from .views import PlantFromSAPView, PlantListView, CustomerFromSAPView, CustomerListView

urlpatterns = [
   # plant urls
   path('updatePlant/<str:PLANT>/', PlantFromSAPView.as_view()),
   path('createPlant/', PlantFromSAPView.as_view()),
   path('getAllPlants/', PlantListView.as_view()),
   path('getPlant/<str:PLANT>/', PlantListView.as_view()),

   # customer urls
   path('updateCustomer/<str:CUST_ID>/', CustomerFromSAPView.as_view()),
   path('createCustomer/', CustomerFromSAPView.as_view()),
   path('getAllCustomers/', CustomerListView.as_view()),
   path('getCustomer/<str:CUST_ID>/', CustomerListView.as_view()),
]


