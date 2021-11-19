from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Cart(request):
    return render(request, 'queenok/cart_page.html')
