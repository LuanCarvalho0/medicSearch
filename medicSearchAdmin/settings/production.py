from medicSearchAdmin.settings.settings import *


DEBUG = True

SECRET_KEY = 'f0a2b24c826dd34ecfe1fc3a0fbf6431cf1d0b33e9437a9a'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
