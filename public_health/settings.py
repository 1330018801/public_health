# -*- coding: utf-8 -*-

"""
Django settings for public_health project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q^*6e0l6(=_v+-2lctz+1cm^q@l%w%dj1b51w$-1ar-js0)312'

# SECURITY WARNING: don't run with debug turned on in production!
import socket

if socket.gethostname() == 'web.phis':  # prod environment
    DEBUG = TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['.phis.com.cn']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'sh_health',
            'HOST': '10.1.0.119',
            'USER': 'postgres',
            'PASSWORD': '6yhn7ujm,./',
            'PORT': '5432'
        }
    }
else:  # development environment
    DEBUG = TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    'backend',
    'management',
    'services',
    'education',
    'vaccine',
    'child',
    'pregnant',
    'old',
    'hypertension',
    'diabetes',
    'psychiatric',
    'tcm',
    'infectious',
    'supervision',
    'ehr',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'public_health.urls'
WSGI_APPLICATION = 'public_health.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

LOGIN_URL = '/'

DJANGO_LOG_LEVEL = DEBUG

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s]%(levelname)s(%(name)s): %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s]%(levelname)s(%(name)s): %(message)s'
        },
    },
    'handlers': {
        # 'file': {
        #    'class': 'logging.FileHandler',
        #    'filename': os.path.join(BASE_DIR, 'log/site.log'),
        #    'formatter': 'verbose'
        #},
        'console': {
            'level': DEBUG,
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        # 'django': {
        #    'handlers': ['file'],
        #    'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        #},
        'debug': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        #'django.request': {
        #    'handlers': ['file'],
        #    'level': 'DEBUG',
        #    'propagate': True,
        #},
    },
}

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'images/')
MEDIA_URL = '/medias/'

