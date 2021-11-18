from django.contrib import admin
from django.urls import path, include

from User import views

urlpatterns = [
    # path('login&register/', views.Login),
    path('accounts/', include('django.contrib.auth.urls')),
]
