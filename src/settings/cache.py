from settings._from_env import (
    _REDIS_HOST,
    _REDIS_PORT,
)


REDIS_HOST = _REDIS_HOST

REDIS_PORT = _REDIS_PORT

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}",
        "TIMEOUT": 1_209_600,  # 2 weeks
        "KEY_PREFIX": "devices_project",
    }
}
