"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

<<<<<<< HEAD
from django.core.asgi import get_asgi_application
# from channels.routing import get_default_application
import django 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
django.setup()
# application = get_default_application()
=======
# from django.core.asgi import get_asgi_application
from channels.routing import get_default_application
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
application = get_default_application()

# application = get_asgi_application()
>>>>>>> 41e547da9de11c963a2b35eed6aafd683537d30a
