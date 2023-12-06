from medicSearchAdmin.settings.settings import *


DEBUG = True

SECRET_KEY = '6d84e5a8ac63b551de85f6c34d5a13e57b51b9c1c7d729b7'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
