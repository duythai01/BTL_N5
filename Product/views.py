
from django.shortcuts import render
from Product.models import *


def Index(request):
    New_product = Product.objects.all().reverse()
    Women_product = Product.objects.filter(category__name='nu')
    Men_product = Product.objects.filter(category__name='nam')
    Fashion_product = Product.objects.filter(tags__name='fashion')


    return render(request, 'queenok/index.html',
                  {'New_product': New_product,
                   'wm_product': Women_product,
                   'm_product': Men_product,
                   'fs_product': Fashion_product

                   }
                  )


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
