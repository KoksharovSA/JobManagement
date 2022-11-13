from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import *


def home(request):
    posts = HomePage.objects.order_by('-week_number')[0]

    context = {
        'title': 'Главная страница',
        'posts': posts,
    }
    return render(request, 'home/home.html', context)

def show_week(request, number_week):
    post = get_object_or_404(HomePage, week_number=number_week)
    context = {
        'title': '{0} неделя'.format(number_week),
        'posts': post,
    }
    return render(request, 'home/post.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
