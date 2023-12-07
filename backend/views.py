from django.shortcuts import render
from rest_framework import viewsets
from backend.serializers.UserSerializer import UserSerializer, User
from backend.serializers.EventSerializer import EventSerializer, Event
from backend.serializers.LinkSerializer import LinkSerializer, Link
from backend.serializers.EventLinkSerializer import EventLinkSerializer, EventLink
from backend.serializers.UserDetailsSerializer import UserDetailsSerializer, UserDetails
from backend.serializers.UserLinkSerializer import UserLinkSerializer, UserLink


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class EventLinkViewSet(viewsets.ModelViewSet):
    queryset = EventLink.objects.all()
    serializer_class = EventLinkSerializer

class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class UserLinkViewSet(viewsets.ModelViewSet):
    queryset = UserLink.objects.all()
    serializer_class = UserLinkSerializer
