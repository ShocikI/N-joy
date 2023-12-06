from django.db import models
from django.contrib.auth.models import User as AuthUser
from .UserDetails import UserDetails

class User(AuthUser):
    user_details = models.OneToOneField(
        UserDetails, verbose_name=("User"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = ("Users")
        verbose_name_plural = ("Users")
