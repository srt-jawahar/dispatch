from django.urls import path
from .views import FreightView


urlpatterns = [
   # freight urls
   path('freightOrder/', FreightView.as_view()),
]
