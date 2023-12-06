from django.db import models
from .Event import Event
from .Link import Link

class EventLink(models.Model):
    event = models.ForeignKey(Event, verbose_name=("Event"), on_delete=models.CASCADE, blank=False)
    link = models.ForeignKey(Link, verbose_name=("Link"), on_delete=models.CASCADE, blank=False)