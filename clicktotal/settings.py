#encoding:utf-8
# Django settings for myproject project.
# Requisitos y modificaciones
# Tener instalados las siguientes herramientas django:
#   'dajaxice',      --> http://www.dajaxproject.com/ <--- dejo links de referencias a las distintas herramientas
#   'dajax',         --> http://www.dajaxproject.com/
#   'social_auth',   --> http://django-social-auth.readthedocs.org/en/latest/
#   'south',         --> http://south.aeracode.org/
#   'endless_pagination',  --> https://django-endless-pagination.readthedocs.org/en/latest/
# instalar pip install python-dateutil --> para manejar fechas facilmente

# Se agregaron las siguientes partes:
# TEMPLATE_CONTEXT_PROCESSORS
# AUTHENTICATION_BACKENDS
# Configuraciones de social_auth
# Estas se encuentran al final del archivo 

# Revisar datos de la base de datos
# clicktotal es el nombre del proyecto

import os
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Saul Enrrique Pineda Torres', 'enrique_wx@hotmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_cupon',                      # Or path to database file if using sqlite3.
        'USER': 'viewor',                      # Not used with sqlite3.
        'PASSWORD': 'viewor_12',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Mexico_City'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-Mx'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'../public/upload')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
     os.path.join(RUTA_PROYECTO,'../public/static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'luk9v-*y0hy46)9!#2%*1wa(%)ebp!k3m3myca&amp;t9=17zen8yh'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'clicktotal.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'clicktotal.wsgi.application'

TEMPLATE_DIRS = (
     os.path.join(RUTA_PROYECTO,'../public/templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'dajaxice',
    'dajax',
    'social_auth',
    'south',
    'endless_pagination',
    'empresa',
    'cupon',
    'usuario',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_login_redirect',

)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY         = 'CtfnQEbeggFbyqQRM53cw'
TWITTER_CONSUMER_SECRET      = 'THZhFvFMVN8iYPdVcLAT9Ig2AwvBrrQTLNjj8PJkD4'
FACEBOOK_APP_ID              = '306615159417586'
FACEBOOK_API_SECRET          = 'a0c086778c72d8fc8c57adfc3b850dde'


LOGIN_URL          = '/#iniciaSecion'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

# Para que despues se cambien los urls
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

# nombre por default?
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'