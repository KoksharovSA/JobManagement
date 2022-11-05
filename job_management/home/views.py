from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def home(request):
    posts = HomePage.objects.all()
    data_active_page = {
        'title': 'Рабочее задание',
        'posts': posts,
        'css_active': 'nav-link px-2 fs-4 fw-bold text-warning',
        'css_nonactive': 'nav-link px-2 fs-4 text-white'
    }
    return render(request, 'home/home.html', data_active_page)

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
