from django.urls import path
from .views import PlantFromSAPView

urlpatterns = [
   path('update/<str:PLANT>/', PlantFromSAPView.as_view()),
   path('create/', PlantFromSAPView.as_view()),
]


