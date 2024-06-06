from django.shortcuts import render
from .models import Movie


def index(request):
    projects = Movie.objects.all()
    return render(request, 'movie/index.html', {'projects': projects})
