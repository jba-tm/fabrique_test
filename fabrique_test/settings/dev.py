from ._base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WEBSITE_URL = "http://127.0.0.1:8000"  # without trailing slash


if 'debug_toolbar' in INSTALLED_APPS:
    MIDDLEWARE += [
        # Debug toolbar

        'debug_toolbar.middleware.DebugToolbarMiddleware',
        # 'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }

    INTERNAL_IPS = [
        # ...
        '127.0.0.1',
        # ...
    ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': get_secret('DATABASE_NAME'),
    #     'USER': get_secret('DATABASE_USER'),
    #     'PASSWORD': get_secret('DATABASE_PASSWORD'),
    #     'HOST': get_secret('DATABASE_HOST'),
    #     'PORT': get_secret('DATABASE_PORT'),
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     }
    # },

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': get_secret('DATABASE_NAME'),
    #     'USER': get_secret('DATABASE_USER'),
    #     'PASSWORD': get_secret('DATABASE_PASSWORD'),
    #     'HOST': 'db',
    #     # 'PORT': int(get_secret('DATABASE_PORT')),
    #     'PORT': 5432,
    # }
}

# ROOT_URLCONF = f'{PROJECT_NAME}.urls'

try:
    from .local import *
except ImportError:
    pass
