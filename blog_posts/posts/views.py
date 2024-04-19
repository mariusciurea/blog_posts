from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.decorators import login_required
from .forms import PostsForm

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


@login_required(login_url='users-login')
def create_post(request):
    # print(request.method)
    # print(request.POST)
    # form_post = PostsForm(request.POST)
    # print(form_post)
    # context = {'form': form_post}
    context = {}
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST.get('content')

        Posts.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        return redirect('posts-home')

    return render(request, 'posts/create-post.html', context)


def about(request):
    return render(request, 'posts/about.html')
