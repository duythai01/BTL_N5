from django.shortcuts import render
from django.http import HttpResponse


def Index(request):
    return render(request, 'queenok/index.html')


def Category(request):
    return render(request, 'queenok/category_page.html')


def ContactUs(request):
    return render(request, 'queenok/contact_us.html')


def Detail(request):
    return render(request, 'queenok/product_detail_page.html')


def SingleBlog(request):
    return render(request, 'queenok/single_blog.html')


def BlogPage(request):
    return render(request, 'queenok/blog_page.html')

def About(request):
    return render(request, 'queenok/about.html')
