"""
Django settings for django_cwm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, glob
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b^t*u5vhgwcrw-q9dy0tqo^^_l@#32=#17ss2^t0wt@a7yg#&9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

SITE_ID = 1

#if DEBUG:
#    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = 'lope.cwm@gmail.com'
# EMAIL_HOST_PASSWORD = 'C=-h>.\WKn[<9/)#}$es-Jl.?7f[(\)^i!:;Z;QR(i\:,pe=uh'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = "25"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = "copens <copens@lopen.linguistics.ntu.edu.tw>"

LOGIN_REDIRECT_URL = 'http://lopen.linguistics.ntu.edu.tw/copens/'

# Application definition

INSTALLED_APPS = (
    'control_panel',
    'api',
    'rest_framework',
    # 'rest_framework.authtoken',
    'django_pygments',
    'django_facebook',
    'about',
    'misc',
    'wordlist',
    'copenAuth',
    'captcha',
    'endless_pagination',
    'registration_custom',
    'registration_defaults',
    'cwm',
    'brat',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

ACCOUNT_ACTIVATION_DAYS = 2 

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_cwm.urls'

WSGI_APPLICATION = 'django_cwm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static_cwm/'
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)),'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_all')

from registration_defaults.settings import *

#TEMPLATE PATH
TEMPLATE_DIRS = (
    REGISTRATION_TEMPLATE_DIR,
    os.path.join(BASE_DIR, 'registration_defaults/templates/registration'), # --> this will override the above path
)

TEMPLATE_DIRS += tuple(glob.glob(os.path.join(BASE_DIR, 'templates/*')))


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'cwm.context_processors.include_search_form',
    'django.contrib.auth.context_processors.auth',
    'django_facebook.context_processors.facebook',
)

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SESSION_COOKIE_AGE = 365 * 24 * 60 * 600

ENDLESS_PAGINATION_PER_PAGE = 100



# URL of the login page.
LOGIN_URL = '/login/'

UPLOAD_FILE_DIRS = os.path.join(BASE_DIR, 'upload_files')


#class InvalidString(str):
#    def __mod__(self, other):
#        from django.template.base import TemplateSyntaxError
#        raise TemplateSyntaxError(
#            "Undefined variable or unknown value for: \"%s\"" % other)
#
#TEMPLATE_STRING_IF_INVALID = InvalidString("%s")

FACEBOOK_APP_ID = '394573580694439'
FACEBOOK_APP_SECRET = 'a6a4a6b43676965156f98655abc0b34b' 

AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
FACEBOOK_LOGIN_DEFAULT_REDIRECT = '/copens' 


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '30/minute'
    },
}

# set forwarded_host to use x_forwarded_host in request.get_host
# USE_X_FORWARDED_HOST = True


# Configuration of Django-logger
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/log/copen/debug.log',
        },
    },
    'loggers': {
        'cwm': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
