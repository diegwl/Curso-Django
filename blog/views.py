from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

def blog(request):
    return HttpResponse('blog')

def exemplo(request):
    return HttpResponse('exemplo')
