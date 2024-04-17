from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('login/', views.login, name='users-login'),
    path('register/', views.register, name='users-register'),
    path('logout/', views.logout, name='users-logout'),
]