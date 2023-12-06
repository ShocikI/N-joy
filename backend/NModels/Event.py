from django.db import models
from .User import User

class Categories():
    PARTY = 0
    CINEMA = 1
    THEATRE = 2
    STAND = 3
    SPECIAL = 4
    SALE = 5

    CATEGORIES = (
        (PARTY, "Party"),
        (CINEMA, "Cinema"),
        (THEATRE, "Theatre"),
        (STAND, "Stand-up"),
        (SPECIAL, "Special event"),
        (SALE, "Sale"),
    )

class Event(models.Model):
    title = models.CharField(max_length=128, blank=False)
    owner = models.ForeignKey(User, verbose_name=("Owner"), on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    category = models.PositiveSmallIntegerField(choices=Categories.CATEGORIES, blank=False)
     
    image = models.ImageField(upload_to="images/posters", height_field=None, width_field=None, max_length=None)
    description = models.TextField(max_length=2048)
    price = models.FloatField(default=0.0)
    avaliable_places = models.IntegerField(default=0)
    init_date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")
