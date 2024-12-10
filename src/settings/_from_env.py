import os
from distutils.util import strtobool


if strtobool(os.getenv("DOTENV_MODE", "false")):
    from dotenv import load_dotenv

    load_dotenv()

# Dadata

_DADATA_API_KEY = os.getenv("DADATA_API_KEY")

_DADATA_SECRET_KEY = os.getenv("DADATA_SECRET_KEY")

# ----------------------------------------------------------------------------------------------------------------------


# Django

_DEBUG = strtobool(os.getenv("DEBUG"))

_SECRET_KEY = os.getenv("SECRET_KEY")

# ----------------------------------------------------------------------------------------------------------------------


# PostgreSQL

_PG_DATABASE_NAME = os.getenv("PG_DATABASE_NAME")

_PG_HOST = os.getenv("PG_HOST")

_PG_PORT = os.getenv("PG_PORT")

_PG_USER_NAME = os.getenv("PG_USER_NAME")

_PG_USER_PASSWORD = os.getenv("PG_USER_PASSWORD")

# ----------------------------------------------------------------------------------------------------------------------


# Redis

_REDIS_HOST = os.getenv("REDIS_HOST")

_REDIS_PORT = os.getenv("REDIS_PORT")
