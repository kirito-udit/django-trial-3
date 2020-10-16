from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_email_verification import urls as mail_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('vid.urls')),
    path('',include('login.urls')),
    path('',include('signup.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('email/', include(mail_urls)),

]

#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)