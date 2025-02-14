from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name="home"),
    path('Aboutus',views.AboutUs,name="aboutus"),
    path('Products',views.Products,name="products")
]
