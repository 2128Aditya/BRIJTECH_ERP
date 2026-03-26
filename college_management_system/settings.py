"""
Django settings for college_management_system project.
"""

import dj_database_url
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# ================= SECURITY =================
SECRET_KEY = 'django-insecure-abc123xyz987-super-secret'

DEBUG = True  # Deploy ke baad False kar dena

ALLOWED_HOSTS = ['*']   # 🔥 FIX


# ================= INSTALLED APPS =================
INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    'main_app.apps.MainAppConfig'
]


# ================= MIDDLEWARE =================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 🔥 FIX (WhiteNoise position)
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # My Middleware
    'main_app.middleware.LoginCheckMiddleWare',
]


ROOT_URLCONF = 'college_management_system.urls'


# ================= TEMPLATES =================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['main_app/templates'],
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


WSGI_APPLICATION = 'college_management_system.wsgi.application'


# ================= DATABASE =================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Production DB (Render)
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


# ================= PASSWORD VALIDATION =================
if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else:
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]


# ================= INTERNATIONAL =================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# ================= STATIC FILES =================
STATIC_URL = '/static/'

# 🔥 FIX
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# optional (recommended)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ================= AUTH =================
AUTH_USER_MODEL = 'main_app.CustomUser'
AUTHENTICATION_BACKENDS = ['main_app.EmailBackend.EmailBackend']


# ================= SESSION =================
SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True


# ================= EMAIL =================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_HOST_USER = "aadi21082003@gmail.com"
EMAIL_HOST_PASSWORD = "ordgcfeispsdphfg"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_USE_TLS = True


# ================= STATIC OPTIMIZATION =================
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'