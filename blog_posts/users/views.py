from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return HttpResponse("<h1>This is the login page</h1>")


def register(request):
    pass


def logout(request):
    pass
