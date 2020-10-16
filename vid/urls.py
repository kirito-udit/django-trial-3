from django.contrib import admin
from django.urls import path, include, URLPattern
from . import views
#from django.contrib.auth.views import LoginView
import django.contrib.auth.views
urlpatterns = [
    # URL FOR THE THUMBNAIL(HOME) PAGE
    path('', views.thumbnail, name = "home"),
    # URL PATTERN FOR THE PAYPAL PAYMENT PAGE
    path('(?P<title>',views.payment, name = "payment"),
    # URL PATTERN FOR THE GIVEAWAY PAGE
    path('video', views.video,name = "video"),
        # URL PATTERN FOR THE PAID VIDEO PLAYER (DYNAMIC URL MAPPING)
   path('(.?P<title>', views.vidDetails, name = "play"),
       # URL PATTERN FOR THE SEARCH RESULTS PAGE
   path('search/',views.search,name='search'),
   path('play/(?P<title>/comment',views.commentpost, name="comment-post"),
    path('like/(?P<title>', views.likepost, name = "like-post"),
    path('report/(?P<title>', views.reportpost, name = "report-post"),
    path('(/?P<title>', views.vidplay, name = "played"),

]