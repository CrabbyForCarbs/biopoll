# instabio/settings.py

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

# SECURITY WARNING: keep the secret key used in production secret!
# Reads the SECRET_KEY from an environment variable.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-a-temporary-key-for-local-use-only')

# SECURITY WARNING: don't run with debug turned on in production!
# Reads the DEBUG setting from an environment variable. Defaults to False.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Defines the allowed hosts for different environments.
ALLOWED_HOSTS = []

# Add the Vercel deployment URL to the allowed hosts
VERCEL_URL = os.environ.get('VERCEL_URL')
if VERCEL_URL:
    # A more robust way to handle the URL, whether it has https:// or not
    if '://' in VERCEL_URL:
        ALLOWED_HOSTS.append(VERCEL_URL.split('://')[1])
    else:
        ALLOWED_HOSTS.append(VERCEL_URL)

# Add the Render deployment URL to the allowed hosts
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Add local hosts for development if DEBUG is True
if DEBUG:
    ALLOWED_HOSTS.extend(['127.0.0.1', 'localhost'])



# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic', # Added for Whitenoise
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Added for Whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'instabio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'instabio.wsgi.application'


# ==============================================================================
# DATABASE
# ==============================================================================
DATABASES = {
    'default': dj_database_url.config(
        # This reads the DATABASE_URL from your environment.
        # It correctly falls back to SQLite for local development.
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
        # The problematic 'ssl_require=True' line has been removed.
    )
}
# ===================================================================
# PASSWORD VALIDATION
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==============================================================================
# INTERNATIONALIZATION & STATIC FILES
# ==============================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
# This is where collectstatic will gather all static files.
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Using Whitenoise for efficient static file serving.
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'