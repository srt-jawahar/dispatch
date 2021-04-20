from django.urls import path
from .views import RegistrationView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetViaEmail, SetNewPasswordAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('request-reset-email/', RequestPasswordResetViaEmail.as_view(), name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]
