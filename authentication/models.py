from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('User should have username')
        if email is None:
            raise TypeError('User should have email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('Password should not be empty')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    """
    Role is given as choice as a temporary solution. in future we will be moving it a separate table
    """
    roles = (
        ("ROLE_ADMIN", "Admin"),
        ("ROLE_MANAGER", "Freight Order Manager"),
        ("ROLE_SPECIALIST", "Freight Order Specialist"),
        ("ROLE_PLANNING_SPECIALIST", "Freight Planning Specialist"),
        ("ROLE_PLANNING_MANAGER", "Freight Planning Manager"),
        ("ROLE_TRACKER", "Tracker"),
        ("ROLE_FINAL_MANAGER", "Manager"),
    )

    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=50, unique=True, db_index=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(choices=roles, max_length=255, default='ROLE_MANAGER')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh_token = RefreshToken.for_user(self)
        return {
            'refresh_token': str(refresh_token),
            'access_token': str(refresh_token.access_token)
        }
