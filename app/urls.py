from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
]