from django.shortcuts import render
from django.http import HttpResponse


def Order(request):
    return render(request, 'queenok/checkout_page.html')
