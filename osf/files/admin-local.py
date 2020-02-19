from . import defaults
import os

OSF_URL = os.environ['OSF_SERVICE_URL']

ALLOWED_HOSTS = [
    os.environ['ALLOWED_HOST']
]

UNSUPPORTED_FORCE_TO_USE_ADDONS = [
    'github',
    'wiki',
    'figshare',
    'mendeley',
    'box',
    's3',
    'googledrive',
    'owncloud',
    'azureblobstorage',
    'dropbox',
    'jupyterhub',
    'dataverse',
    'osfstorage',
    'zotero',
    'bitbucket',
    'swift',
    'weko',
    's3compat',
    'nextcloud',
    'gitlab',
    'onedrive'
]

FCM_SETTINGS = {
    "FCM_SERVER_KEY": os.environ['FCM_SERVER_KEY']
}
SESSION_COOKIE_DOMAIN = os.environ['OSF_COOKIE_DOMAIN']
CSRF_COOKIE_DOMAIN = os.environ['OSF_COOKIE_DOMAIN']
CSRF_TRUSTED_ORIGINS = [
    '.' + os.environ['OSF_COOKIE_DOMAIN']
]
ENABLE_LOGIN_FORM = os.environ['USE_LOGIN_FORM']
ENABLE_SHB_LOGIN = os.environ['USE_SHB_LOGIN']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['MAIL_SERVER']
EMAIL_PORT = os.environ['MAIL_PORT']
EMAIL_HOST_USER = os.environ['MAIL_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['MAIL_PASSWORD']
EMAIL_USE_TLS = os.environ['MAIL_USE_TLS']
