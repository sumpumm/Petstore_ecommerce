from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name="home"),
    path('login',views.login,name="login"),
]
