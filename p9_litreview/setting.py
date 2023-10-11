# Importing the necessary modules
import os
from pathlib import Path

# Importing constants from Django messages module
from django.contrib.messages import constants as message_constants

# Getting the base directory of the project using pathlib module
BASE_DIR = Path(__file__).resolve().parent.parent

# Setting the secret key for the Django project
SECRET_KEY = 'django-insecure-^3d8hi=(g$(ngj8#8%rm(!4_ams**a(hx$b*df%j%#_60hjy0t'

# Setting the debug mode to True
DEBUG = True

# Allowing all hosts to access the Django project
ALLOWED_HOSTS = []

# List of installed apps for the Django project
INSTALLED_APPS = [
    'reviews.apps.ReviewsConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# List of middleware classes for the Django project
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# The root URL configuration module for the Django project
ROOT_URLCONF = 'LITReview.urls'

# Template settings for the Django project
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# The WSGI application module for the Django project
WSGI_APPLICATION = 'LITReview.wsgi.application'

# Message tags for the Django project
MESSAGE_TAGS = {message_constants.ERROR: 'danger'}

# Database configuration for the Django project
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings for the Django project
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Language code for the Django project
LANGUAGE_CODE = 'en-us'

# Time zone for the Django project
TIME_ZONE = 'CET'

# Enable internationalization for the Django project
USE_I18N = True

# Enable localization for the Django project
USE_L10N = True

# Enable timezone support for the Django project
USE_TZ = True

# Static files URL for the Django project
STATIC_URL = '/static/'

# Media root directory for file uploads in the Django project
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Template pack for crispy forms in the Django project
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Default auto field for the Django project
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URL to redirect after successful login
LOGIN_REDIRECT_URL = 'reviews-feed'

# URL for the login page
LOGIN_URL = 'login'
