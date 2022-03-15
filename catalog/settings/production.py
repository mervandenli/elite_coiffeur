from catalog.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'istanbulcoiffeurdb',
        'USER': 'mervandenli',
        'PASSWORD': '@Elite:123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')