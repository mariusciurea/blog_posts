from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from posts.models import Posts
# Create your views here.


def user_login(request):
    user_type = 'login'
    if request.user.is_authenticated:
        return redirect('posts-home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('posts-home')
            else:
                messages.error(request, 'Username or password does not exist!')

        except Exception:
            messages.error(request, 'User does not exist!')
    context = {'type': user_type}
    return render(request, 'users/user_login.html', context)


def user_register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('posts-home')

    context = {'form': form}

    return render(request, 'users/user_login.html', context)


def user_profile(request):
    posts = Posts.objects.filter(user=request.user)
    print(request.user)
    print(posts)
    context = {'posts': posts}
    return render(request, 'users/profile.html', context)


def user_logout(request):
    logout(request)
    return redirect('posts-home')
