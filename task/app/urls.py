from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('events/',views.events, name='events'),
    path('proposal/',views.proposal, name='proposal'),
    path('register/',views.register, name='register'),
    path('succes/', views.succes, name='succes'),
    path('regsucces/', views.regsucces, name='regsucces'),
    path('delete/<int:id>/', views.Delete, name='delete'),
    path('edit/<int:id>/', views.Edit_event, name='edit'),
]


