from ._base import *

DEBUG = False


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': get_secret('DATABASE_NAME'),
    #     'USER': get_secret('DATABASE_USER'),
    #     'PASSWORD': get_secret('DATABASE_PASSWORD'),
    #     'HOST': get_secret('DATABASE_HOST'),
    #     'PORT': get_secret('DATABASE_PORT'),
    # },

    # 'default': {
    #     # 'ENGINE': 'django.db.backends.postgresql',
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': get_secret('DATABASE_NAME'),
    #     'USER': get_secret('DATABASE_USER'),
    #     'PASSWORD': get_secret('DATABASE_PASSWORD'),
    #     'HOST': get_secret('DATABASE_HOST'),
    #     # 'HOST': 'db',
    #     # 'PORT': get_secret('DATABASE_PORT'),
    #     'PORT': 5432,
    # },
}


try:
    from .local import *
except ImportError:
    pass
