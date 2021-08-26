"""
Django settings for pyui project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, socket, logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jlk7u+v6mqq$(47=*us23ru^tx$x3sj^+$314htmpperz)a7@b'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DJANGO_DEBUG') is None or os.environ.get('DJANGO_DEBUG').lower() == 'true':
    print("Debug is enabled.")
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyui.urls'

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

WSGI_APPLICATION = 'pyui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

##############################################################

REGISTRY_URL = os.environ.get('REGISTRY_URL','http://localhost:8761/eureka/apps')

SERVICES_HOST = os.environ.get('SERVICES_HOST','localhost')
SERVICES_PORT = os.environ.get('SERVICES_PORT','8080')
SERVICES_CLIENT_ID = os.environ.get('auth.client.id','web-client')
SERVICES_CLIENT_SECRET = os.environ.get('auth.client.secret','secret')

SERVICES_ENDPOINT = 'http://'+SERVICES_HOST+':'+SERVICES_PORT

if os.environ.get('DJANGO_DEBUG') is None or os.environ.get('DJANGO_DEBUG').lower() == 'true':
    ADMIN_ENDPOINT = 'http://localhost:8081'
    AUTH_ENDPOINT = 'http://localhost:8082'
    PRODUCT_ENDPOINT = 'http://localhost:8083'
    ORDER_ENDPOINT = 'http://localhost:8084'
    INVENTORY_ENDPOINT = 'http://localhost:8085'
else:
    ADMIN_ENDPOINT = SERVICES_ENDPOINT
    AUTH_ENDPOINT = SERVICES_ENDPOINT
    PRODUCT_ENDPOINT = SERVICES_ENDPOINT
    ORDER_ENDPOINT = SERVICES_ENDPOINT
    INVENTORY_ENDPOINT = SERVICES_ENDPOINT

HTTP_TIMEOUT = 20
HTTP_SAMPLE_DATA_TIMEOUT = 120

LOG_FILE=os.environ.get('PYUI_LOG_FILE','./PyUi.log')
LOG_LEVEL=os.environ.get('PYUI_LOG_LEVEL','INFO')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {"()": "pythonjsonlogger.jsonlogger.JsonFormatter"},
        'verbose': {
            'format': 'time=%(asctime)s.%(msecs)03d  GMT+05:30 level=%(levelname)s hostname=%(hostname)s '
                      'service=PyUI threadId=%(thread)d class=%(module)s pid=%(process)d message=%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(asctime)s.%(msecs)03d %(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'custom_filter': {
            '()': 'app.ext.logfilter.AppLogFilter',
        }
    },
    'handlers': {
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filters': ['require_debug_true','custom_filter'],
            'filename': LOG_FILE,
            'formatter': 'verbose',
        },
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true','custom_filter'],
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file','console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file','console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'django.utils.autoreload': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'app': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'

