from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='index'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
