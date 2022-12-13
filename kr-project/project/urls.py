"""project URL Configuration

The `urlpatterns` list routes URLs to views. """

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('domain/', include('re_domain.urls')),
    path('api/', include('api.urls'))
]
