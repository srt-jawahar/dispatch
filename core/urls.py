
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Dispatch Planner API",
      default_version='v1',
      description="Plans delivery simpler than ever",
      contact=openapi.Contact(email="foucsrdeployment@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
