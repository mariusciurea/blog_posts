from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

dummy_posts = [
    {
        'id': 1,
        'title': 'post number 1',
        'content': 'post content 1'
    },

    {
        'id': 2,
        'title': 'post number 2',
        'content': 'post content 2'
    },

    {
        'id': 3,
        'title': 'post number 3',
        'content': 'post content 3'
    }
]


def home(request):
    # return HttpResponse('<h1>Welcome to my blog!</h1>')
    context = {'posts': dummy_posts}
    return render(request, 'home.html', context)


def about(request):
    return HttpResponse('<h1>This is my About page!</h1>')
