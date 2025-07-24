from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'About us',
        'text_on_page': 'sample'
    }
    return render(request, 'main/about.html', context=context)
