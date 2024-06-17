from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'movie/home.html')


def logoutuser(request):  # Выйти
    if request.method == "POST":
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'movie/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'movie/login.html',
                          {'form': AuthenticationForm(), 'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')


def index(request):
    projects = Movie.objects.all()
    return render(request, 'movie/index.html', {'projects': projects})


def signupuser(request):
    if request.method == "GET":
        return render(request, 'movie/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'movie/signupuser.html',
                              {'form': UserCreationForm(), 'error': "Такое имя пользователя уже существует"})
        else:
            return render(request, 'movie/signupuser.html',
                          {'form': UserCreationForm(), 'error': "Пароли не совпадают"})


def currenttodes(request):
    return render(request, 'movie/currenttodes.html')
