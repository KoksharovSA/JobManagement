from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def home(request):
    posts = HomePage.objects.all()
    return render(request, 'home/home.html', {'title': 'Главная страница',
                                              'css_active': 'nav-link px-2 fs-4 fw-bold text-warning',
                                              'css_nonactive': 'nav-link px-2 fs-4 text-white',
                                              'posts': posts})

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
