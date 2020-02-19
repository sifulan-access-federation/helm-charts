from .defaults import *  # noqa
from website import settings as osf_settings

import os

# NOTE:
# https://docs.djangoproject.com/en/1.8/ref/settings/#secure-proxy-ssl-header
# http://stackoverflow.com/questions/22279893/djangorestframework-https-links-with-routers-and-viewsets
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

JWT_SECRET = os.environ['CAS_JWT_SECRET']
JWE_SECRET = os.environ['CAS_JWE_SECRET']
BYPASS_THROTTLE_TOKEN = os.environ['BYPASS_THROTTLE_TOKEN']
HASHIDS_SALT = os.environ['HASHIDS_SALT']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = [
    os.environ['ALLOWED_HOST']
]

STATIC_URL = '/v2/static/'

#DEBUG = osf_settings.DEBUG_MODE
DEBUG = False
VARNISH_SERVERS = [
    os.environ['OSF_VARNISH_SERVERS']
]
ENABLE_VARNISH = False
ENABLE_ESI = False
CORS_ORIGIN_ALLOW_ALL = True

# Uncomment to get real tracebacks while testing
# DEBUG_PROPAGATE_EXCEPTIONS = True

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar', )
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda(_): True
    }
    ALLOWED_HOSTS.append('localhost')

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'user': '1000000/second',
    'non-cookie-auth': '1000000/second',
    'add-contributor': '1000000/second',
    'create-guid': '1000000/second',
    'root-anon-throttle': '1000000/second',
    'test-user': '2/hour',
    'test-anon': '1/hour',
}

# UPKI flag
USE_UPKI = os.environ['USE_UPKI']

#uPKI operation commands
UPKI_TIMESTAMP_URL = os.environ['UPKI_TIMESTAMP_URL']
UPKI_CREATE_TIMESTAMP = os.environ['UPKI_CREATE_TIMESTAMP']
UPKI_VERIFY_TIMESTAMP = os.environ['UPKI_VERIFY_TIMESTAMP']

