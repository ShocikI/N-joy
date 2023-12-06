from django.db import models
from .User import User
from .Link import Link

class UserLink(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE, blank=False)
    link = models.ForeignKey(Link, verbose_name=("Link"), on_delete=models.CASCADE, blank=False)