from django.contrib import admin
from django.urls import path
from Product import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('contact_us', views.ContactUs, name='contact'),
    path('categories', views.Category, name='category'),
    path('detail', views.Detail, name='detail_product'),
    path('blog', views.BlogPage, name='blog'),
    path('single_blog', views.SingleBlog, name='singleblog'),
    path('about', views.About, name='about'),

]
