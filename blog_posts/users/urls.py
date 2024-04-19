from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('login/', views.user_login, name='users-login'),
    path('register/', views.user_register, name='users-register'),
    path('logout/', views.user_logout, name='users-logout'),
    path('profile/', views.user_profile, name='users-profile'),
]