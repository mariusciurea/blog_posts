
from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name='posts-home'),
    path('about/', views.about, name='posts-about'),
    path('post/<str:pk>', views.post, name='posts-post'),
    path('create-post/', views.create_post, name='posts-create-post'),
]