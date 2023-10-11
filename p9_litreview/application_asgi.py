# Importing the necessary module
import os

# Importing the get_asgi_application function from the django.core.asgi module
from django.core.asgi import get_asgi_application

# Setting the DJANGO_SETTINGS_MODULE environment variable to 'LITReview.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LITReview.settings')

# Getting the ASGI application for the Django project
application = get_asgi_application()
