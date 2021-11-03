from django.contrib import admin
from django.urls import path

from Order import views

urlpatterns = [
    path('order/', views.Order, name='order'),
]
