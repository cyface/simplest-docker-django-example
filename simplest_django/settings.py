# Django Settings

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# You must set the SECRET_KEY environment variable before running this project
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True

MAGIC_MESSAGE = os.environ.get("MAGIC_MESSAGE")

ALLOWED_HOSTS = ['django', 'localhost']
INSTALLED_APPS = [
    'simplest_django'
]

ROOT_URLCONF = 'simplest_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
            ],
        },
    },
]

WSGI_APPLICATION = 'simplest_django.wsgi.application'
