from .base import *

SECRET_KEY = '@=#(qnd8@h)8^3!hvp@vov-i=(eh@t_qq97+_!zz=sikep^uze'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}