from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello')


def person(request, name):
    print(request.GET)
    return HttpResponse(f'<h1>Данные</h1><p>{name}</p>')


def product(request):
    return HttpResponse('List products')

def product_buy(request):
    return HttpResponse('prise')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

