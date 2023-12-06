from django.contrib import admin
from .NModels.Event import Event
from .NModels.UserDetails import UserDetails
from .NModels.User import User
from .NModels.Link import Link
from .NModels.UserLink import UserLink
from .NModels.EventLink import EventLink

# Register your models here.
admin.site.register(Event)
admin.site.register(UserDetails)
admin.site.register(User)
admin.site.register(Link)
admin.site.register(UserLink)
admin.site.register(EventLink)