"""
WSGI config for seshat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

local_env_path = str(Path.cwd()) + "/seshat/settings/.env"
if os.path.exists(local_env_path):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seshat.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seshat.settings.base')

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
