from django.contrib import admin
from django.urls import path, include, URLPattern
from . import views
#from django.contrib.auth.views import LoginView
import django.contrib.auth.views
urlpatterns = [
    path('gallery', views.thumbnail, name = "home"),
    path('',views.payment, name = "payment"),
    path('video', views.video,name = "video"),
   path('play/(?P<title>/', views.vidDetails, name = "play"),
   path('search/',views.search,name='search'),

    
]