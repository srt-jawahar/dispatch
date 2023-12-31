from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import RegistrationView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetViaEmail, \
    SetNewPasswordAPIView, LogoutAPIView, GetAllUsersView, ChangePasswordView, UpdateProfileView, \
    UserAvatarUpload, GetAUserView, RoleListView, RoleUpdateRetrieveView, UserStatusView, AdminUserUpdateView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('request-reset-password/', RequestPasswordResetViaEmail.as_view(), name="request-reset-password"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('getAllUsers/', GetAllUsersView.as_view(), name="logout"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path("user-avatar/", UserAvatarUpload.as_view(), name="rest_user_avatar_upload"),
    path("user/<int:pk>/", GetAUserView.as_view(), name="user_get_details"),
    path("role/", RoleListView.as_view(), name="role_get_details"),
    path("role/<int:pk>/", RoleUpdateRetrieveView.as_view(), name="role_get_details"),
    path("user_status/<int:pk>/", UserStatusView.as_view(), name="user_status"),
    path("user_update/<int:pk>/", AdminUserUpdateView.as_view(), name="admin_user_update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
