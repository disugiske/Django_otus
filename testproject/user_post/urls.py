from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.urls import path, include

urlpatterns = [
    path('', index, name="list"),
]
