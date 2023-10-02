'''PROJECT INTRODUCTION:
Eskak - Monitor & Track Electricity Units
---------------------------------------------
    Project Success Criteria(~Milestones~)
        (1) Database Driven Component/s
        (2) User can login or register -
            A logged in user has more access to the small web app
        (3) Website Published using personal Tech Stack(See readme file for explanation!) 😎

TASK 23 | LEVEL 2 | SOFTWARE ENGINEERING
---------------------------------------------
    Made with ❤️. -Branden van Staden

PROJECT SETTINGS
--------------------'''
# IMPORTS
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*&d4=n5vf^)x8wsou_m6bh(r69osd_q87((5=gds4aym6h1w!q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [

]

# Application definition
INSTALLED_APPS = [
    'eskak', # Eskak Application(MAIN)
    'users', # Users Application
    'django.contrib.admin', # Admin Functionality
    'django.contrib.auth', # User Auth
    'django.contrib.contenttypes', # User Roles
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Handles Session Requests(entire app)
    'django.contrib.sessions.middleware.SessionMiddleware', # Associates User with Their Session Requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myEskak.urls'

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

WSGI_APPLICATION = 'myEskak.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''CODE IMPLEMENTED & CONTRIBUTED BY: BRANDEN VAN STADEN'''
