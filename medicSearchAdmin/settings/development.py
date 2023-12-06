from medicSearchAdmin.settings.settings import *


DEBUG = True

SECRET_KEY = 'b674db670cc747f85363a6f9c0d3e3d2080d20a51c4c1a7a'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
