from django.shortcuts import render
from .models import Skils


def index(request):
    projects = Skils.objects.all()
    return render(request, 'skils/index.html', {'projects': projects})
