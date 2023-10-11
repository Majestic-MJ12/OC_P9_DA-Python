# Importing the necessary module
import os

# Importing the get_wsgi_application function from the django.core.wsgi module
from django.core.wsgi import get_wsgi_application

# Setting the DJANGO_SETTINGS_MODULE environment variable to 'LITReview.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LITReview.settings')

# Getting the WSGI application for the Django project
application = get_wsgi_application()
