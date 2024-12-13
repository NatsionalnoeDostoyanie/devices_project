from settings._from_env import (
    _REDIS_HOST,
    _REDIS_PORT,
)


REDIS_DEFAULT_KEY_PREFIX = "devices_project:"

REDIS_DEFAULT_TIMEOUT = 1_209_600  # 2 weeks

REDIS_HOST = _REDIS_HOST

REDIS_PORT = int(_REDIS_PORT)  # type: ignore[arg-type]
