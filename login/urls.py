from django.contrib import admin 
from django.urls import path, include 
# from login import views as user_view
from django.contrib.auth import views as auth 
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('',views.intro),
    path('logout', views.pagelogout, name='logout'),
]