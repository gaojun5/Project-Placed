"""
WSGI config for placed_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Custom settings for 176.31.196.173
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "placed_backend.settings_devserver")

application = get_wsgi_application()
