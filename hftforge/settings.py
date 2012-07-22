# WebSite configuration

PREFIX = ''

TIME_ZONE     = 'Europe/Paris'
LANGUAGE_CODE = 'fr-fr'
USE_I18N      = True
USE_L10N      = True

MEDIA_URL          = PREFIX + "/media/"
STATIC_URL         = PREFIX + "/static/"
ADMIN_MEDIA_PREFIX = PREFIX + "/static/admin/"

# Server configuration

SITE_ID = 1

ADMINS = (
    ('David Delassus', 'david.jose.delassus@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   'hftforge.db',
        # unused for sqlite3
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

import os

MEDIA_ROOT  = os.path.join(os.getcwd(), "media")
STATIC_ROOT = os.path.join(os.getcwd(), "static")

STATICFILES_DIRS = (
    os.path.join(os.getcwd(), "templates", "static"),
)

TEMPLATE_DIRS = (
    os.path.join(os.getcwd(), "templates"),
)

# Specific Django configuration

SECRET_KEY = '@@sg^w2ofhticf@$9bus^$ftzg%ev1=$i2mn&=k0m3gkquh=f-'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hftforge.urls'

INSTALLED_APPS = (
    # HFTForge applications
    'hftforge.apps.tagging',
    'hftforge.apps.overview',
    'hftforge.apps.forum',
    'hftforge.apps.news',
    'hftforge.apps.issues',

    # Django applications
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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
