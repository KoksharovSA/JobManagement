from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def home(request):
    posts = HomePage.objects.all()
    return render(request, 'home/home.html', {'title': 'Главная страница', 'posts': posts})

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
