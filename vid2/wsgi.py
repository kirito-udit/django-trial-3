"""
WSGI config for vid2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vid2.settings')

application = get_wsgi_application()

from static_ranges import Ranges
from dj_static import Cling, MediaCling

application = Ranges(Cling(MediaCling(get_wsgi_application())))