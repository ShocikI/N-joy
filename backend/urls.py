"""
URL configuration for NJoy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'links', views.LinkViewSet)
router.register(r'user_links', views.UserLinkViewSet)
router.register(r'event_links', views.EventLinkViewSet)
router.register(r'user_details', views.UserDetailsViewSet)

urlpatterns = [
   re_path(r'^', include(router.urls))
]
