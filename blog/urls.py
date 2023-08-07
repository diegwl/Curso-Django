from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]
