from django.db import models


class UserDetails(models.Model):
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="images/avatars", blank=True)
    plus = models.IntegerField(default=0)
    minus = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("User Details")
        verbose_name_plural = ("User Details")
