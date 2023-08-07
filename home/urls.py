from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home),
]
