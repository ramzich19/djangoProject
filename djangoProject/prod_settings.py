from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-4_9j*h)#s2zfsn^*unz6o%!p7qgb02p@f1v^v!rhjy%n_@h)@1'


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "185.5.206.149"]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
