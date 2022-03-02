import os
from Silver_ImageGallery.settings.local import *

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
