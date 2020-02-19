# -*- coding: utf-8 -*-
'''Example settings/local.py file.
These settings override what's in website/settings/defaults.py

NOTE: local.py will not be added to source control.
'''

from . import defaults
import os

LOAD_BALANCER = True

#DEV_MODE = True
DEV_MODE = False
#DEBUG_MODE = True # Sets app to debug mode, turns off template caching, etc.
DEBUG_MODE = False # Sets app to debug mode, turns off template caching, etc.
#SECURE_MODE = not DEBUG_MODE  # Disable osf cookie secure
#SECURE_MODE = True
SECURE_MODE = False

#PROTOCOL = 'https://' if SECURE_MODE else 'http://'
PROTOCOL = 'https://'

DOMAIN = os.environ['OSF_SERVICE_URL'] + '/'
INTERNAL_DOMAIN = DOMAIN
API_DOMAIN = os.environ['OSF_API_URL'] + '/'

DB_HOST = os.environ['DB_HOST']

WATERBUTLER_URL = os.environ['OSF_WATERBUTLER_URL']
WATERBUTLER_INTERNAL_URL = WATERBUTLER_URL

ADMIN_URL = os.environ['OSF_ADMIN_URL']
ADMIN_INTERNAL_DOCKER_URL = os.environ['OSF_ADMIN_INTERNAL']

PREPRINT_PROVIDER_DOMAINS = {
    'enabled': False,
    'prefix': 'http://local.',
    'suffix': ':4201/'
}
USE_EXTERNAL_EMBER = True
PROXY_EMBER_APPS = True
EMBER_DOMAIN = os.environ.get('EMBER_DOMAIN', 'localhost')
LIVE_RELOAD_DOMAIN = 'http://{}:4200'.format(EMBER_DOMAIN)  # Change port for the current app
EXTERNAL_EMBER_APPS = {
    'ember_osf_web': {
        'server': 'http://{}/ember_osf_web/'.format(EMBER_DOMAIN),
        'path': '/ember_osf_web/',
        'routes': [
            'collections',
            'handbook',
        ],
    },
    'preprints': {
        'server': 'http://{}:4201/'.format(EMBER_DOMAIN),
        'path': '/preprints/'
    },
    'registries': {
        'server': 'http://{}:4202/'.format(EMBER_DOMAIN),
        'path': '/registries/'
    },
    'reviews': {
        'server': 'http://{}:4203/'.format(EMBER_DOMAIN),
        'path': '/reviews/'
    },
}
EXTERNAL_EMBER_SERVER_TIMEOUT = 600

SEARCH_ENGINE = 'elastic'
ELASTIC_URI = os.environ['ELASTIC_URI']
ELASTIC_TIMEOUT = 10

ENABLE_OSF_HELP = False

# Comment out to use celery in development
USE_CELERY = True

# Email
USE_EMAIL = True
FROM_EMAIL = os.environ['FROM_EMAIL']
#FROM_EMAIL = 'openscienceframework-noreply@osf.nii.ac.jp'
SUPPORT_EMAIL = 'rdm_support@nii.ac.jp'
TO_EMAIL_FOR_DEBUG = None

# Mailchimp email subscriptions
ENABLE_EMAIL_SUBSCRIPTIONS = False

# Session
COOKIE_NAME = 'osf'
OSF_COOKIE_DOMAIN = os.environ['OSF_COOKIE_DOMAIN']
SECRET_KEY = os.environ['SECRET_KEY']
#SESSION_COOKIE_SECURE = SECURE_MODE
SESSION_COOKIE_SECURE = True
OSF_SERVER_KEY = None
OSF_SERVER_CERT = None

##### Celery #####
## Default RabbitMQ broker
#BROKER_URL = os.environ['BROKER_URL']

# Default RabbitMQ backend
#CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']

CELERY_TIMEZONE = 'UTC'

USE_CDN_FOR_CLIENT_LIBS = False

CAS_SERVER_URL = os.environ['OSF_CAS_URL']

# SMTP Settings
MAIL_SERVER = os.environ['MAIL_SERVER']
MAIL_PORT = os.environ['MAIL_PORT']
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']

# Google Analytics
GOOGLE_ANALYTICS_ID = os.environ['GOOGLE_ANALYTICS_ID']
GOOGLE_SITE_VERIFICATION = os.environ['GOOGLE_SITE_VERIFICATION']

# WaterButler Settings
#WATERBUTLER_URL = os.environ['OSF_WATERBUTLER_URL']

# additional setting is mandatory if DEV_MODE is false.
WATERBUTLER_JWE_SECRET = os.environ['WATERBUTLER_JWE_SECRET']
WATERBUTLER_JWE_SALT = os.environ['WATERBUTLER_JWE_SALT']

WATERBUTLER_JWT_SECRET = os.environ['WATERBUTLER_JWT_SECRET']

#WATERBUTLER_JWT_SALT = os.environ['WATERBUTLER_JWT_SALT']
#JWE_SECRET = os.environ['JWE_SECRET']

JWT_SECRET = os.environ['JWT_SECRET']

SENSITIVE_DATA_SALT = os.environ['SENSITIVE_DATA_SALT']
SENSITIVE_DATA_SECRET = os.environ['SENSITIVE_DATA_SECRET']

DB_PASS = os.environ.get('OSF_DB_PASSWORD', '')
#DB_PASS = '-osf-secret-db-pass'
DEFAULT_HMAC_SECRET = os.environ['DEFAULT_HMAC_SECRET']

# project page resource id (e.g. https://osf.nii.ac.jp/t9sg6 -> t9sg6)
POPULAR_LINKS_NODE = 'changeme' # e.g. nrha9
NEW_AND_NOTEWORTHY_LINKS_NODE = 'changeme' # e.g. t9sg6

# MFR Settings
MFR_SERVER_URL = os.environ['OSF_MFR_URL']

LOG_PATH = '/tmp/'

# Keen IO Settings
KEEN = {
    'public': {
        'project_id': os.environ['KEEN_PUBLIC_PROJECT_ID'],
        'master_key': os.environ['KEEN_PUBLIC_MASTER_KEY'],
        'write_key': os.environ['KEEN_PUBLIC_WRITE_KEY'],
        'read_key': os.environ['KEEN_PUBLIC_READ_KEY'],
    },
    'private': {
        'project_id': '',
        'write_key': '',
        'read_key': '',
    },
}

OSF_LOGO = 'rdm_banner'
OSF_PREPRINTS_LOGO = 'osf_preprints'
OSF_MEETINGS_LOGO = 'osf_meetings'
OSF_PREREG_LOGO = 'osf_prereg'
OSF_REGISTRIES_LOGO = 'osf_registries'
OSF_LOGO_LIST = [OSF_LOGO, OSF_PREPRINTS_LOGO, OSF_MEETINGS_LOGO, OSF_PREREG_LOGO, OSF_REGISTRIES_LOGO]

USER_TIMEZONE = 'Asia/Tokyo'
USER_LOCALE = 'ja'

# use Groups on Cloud Gateway
#CLOUD_GATAWAY_HOST = os.environ['CLOUD_GATAWAY_HOST']
# Prefix of isMemberOf attribute for groups
# ex. ISMEMBEROF_GROUP_PREFIX = 'https://cg.gakunin.jp/gr/'
#CLOUD_GATAWAY_ISMEMBEROF_PREFIX = os.environ['CLOUD_GATAWAY_ISMEMBEROF_PREFIX']

# Path of .cer and . key for GakuNin SP on the container of server.
# (for API of Cloud Gateway)
GAKUNIN_SP_CERT = '/ssl/gakunin-sp.cer'
GAKUNIN_SP_KEY  = '/ssl/gakunin-sp.key'

# Settings for mAP core API
MAPCORE_HOSTNAME = os.environ['MAPCORE_HOSTNAME']
MAPCORE_AUTHCODE_PATH = '/oauth/shib/authrequest.php'
MAPCORE_TOKEN_PATH = '/oauth/token.php'
MAPCORE_API_PATH = '/api2/v1'
MAPCORE_AUTHCODE_MAGIC = os.environ['MAPCORE_AUTHCODE_MAGIC']
MAPCORE_CLIENTID = os.environ['MAPCORE_CLIENTID']
MAPCORE_SECRET = os.environ['MAPCORE_SECRET']

ENABLE_USER_MERGE = False
ENABLE_PRIVATE_SEARCH = True
ENABLE_MULTILINGUAL_SEARCH = True
