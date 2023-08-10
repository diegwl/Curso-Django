from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name="index"),
]
