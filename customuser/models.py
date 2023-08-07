from django.contrib.auth.models import AbstractUser
from django.db import models
# managers.py

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, username=None, password=None, **extra_fields):
        if not email and not username:
            raise ValueError('At least one of email or username is required.')

        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # if email and not username:
        #     extra_fields['username'] = None
        #
        # elif username and not email:
        #     extra_fields['email'] = None

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


# class customUser(AbstractUser):
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    objects = CustomUserManager()
