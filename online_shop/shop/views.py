from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def shop(request):
    context = {}
    return render(request, 'shop/shop.html', context)


def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)


def chekout(request):
    context = {}
    return render(request, 'shop/chekout.html', context)

