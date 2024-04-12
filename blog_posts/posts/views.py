from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


# dummy_posts = [
#     {
#         'id': 1,
#         'title': 'post number 1',
#         'content': 'post content 1'
#     },
#
#     {
#         'id': 2,
#         'title': 'post number 2',
#         'content': 'post content 2'
#     },
#
#     {
#         'id': 3,
#         'title': 'post number 3',
#         'content': 'post content 3'
#     }
# ]


def home(request):
    # return HttpResponse('<h1>Welcome to my blog!</h1>')
    posts = Posts.objects.all()
    print(posts)
    # for post in posts:
    #     print(post.title)
    #     print(post.content)
    context = {'posts': posts}
    return render(request, 'posts/home.html', context)


def post(request, pk):
    post = Posts.objects.get(pk=int(pk))
    context = {'post': post}

    return render(request, 'posts/posts.html', context)

def about(request):
    return render(request, 'posts/about.html')
