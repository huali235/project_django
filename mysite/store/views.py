from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def products(request):
    context = {}
    return render(request, 'store/products.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
