import os

from settings._from_env import (
    _DEBUG,
    _SECRET_KEY,
)


ALLOWED_HOSTS: list[str] = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = _DEBUG

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "core.urls"

SECRET_KEY = _SECRET_KEY

WSGI_APPLICATION = "core.wsgi.application"
