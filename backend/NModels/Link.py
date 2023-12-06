from django.db import models

class LinkType():
    FACEBOOK = 0
    X = 1
    INSTAGRAM = 2
    YOUTUBE = 3
    LINKEDIN = 4
    TIKTOK = 5

    LINKS = (
        (FACEBOOK, "Facebook"),
        (X, "X"),
        (INSTAGRAM, "Instagram"),
        (YOUTUBE, "Youtube"),
        (LINKEDIN, "LinkedIn"),
        (TIKTOK, "TikTok"),
    )

class Link(models.Model):
    type = models.SmallIntegerField(choices=LinkType.LINKS, blank=False)
    url = models.TextField(blank=False)