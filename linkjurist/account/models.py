from typing import Any
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models

from django.utils import timezone

# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, name, surname, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to='acc_avatars', blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, default='')

    address = models.CharField(max_length=255, blank=True, default='')
    zip = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=255, blank=True, default='')
    country = models.CharField(max_length=255, blank=True, default='')

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [name, email]
