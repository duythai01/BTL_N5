from django.shortcuts import render
from django.http import HttpResponse


def Login(request):
    return render(request, 'queenok/login.html')
