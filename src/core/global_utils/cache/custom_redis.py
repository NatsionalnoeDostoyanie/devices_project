from typing import (
    Any,
    Awaitable,
    TypeVar,
)

from django.conf import settings
from redis.typing import (
    EncodableT,
    ExpiryT,
    FieldT,
    ResponseT,
)

from core.global_utils.cache.redis_singletons import RedisSingleton


_KeyT = TypeVar("_KeyT", bytes, str)


class CustomRedis(RedisSingleton):
    DEFAULT_KEY_PREFIX = settings.REDIS_DEFAULT_KEY_PREFIX  # type: ignore[misc]
    DEFAULT_TIMEOUT = settings.REDIS_DEFAULT_TIMEOUT  # type: ignore[misc]

    def __init__(
        self,
        host: str = settings.REDIS_HOST,  # type: ignore[misc]
        port: int = settings.REDIS_PORT,  # type: ignore[misc]
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(host, port, *args, **kwargs)

    def prefixed_setex(
        self, name: _KeyT, value: EncodableT, time: ExpiryT = DEFAULT_TIMEOUT, prefix: _KeyT = DEFAULT_KEY_PREFIX
    ) -> ResponseT:
        return self.setex(prefix + name, time, value)

    def prefixed_get(self, name: _KeyT, prefix: _KeyT = DEFAULT_KEY_PREFIX) -> ResponseT:
        return self.get(prefix + name)

    def prefixed_rpush(self, name: str, *values: FieldT, prefix: str = DEFAULT_KEY_PREFIX) -> Awaitable[int] | int:
        return self.rpush(prefix + name, *values)

    def prefixed_lrange(
        self, name: str, start: int, end: int, prefix: str = DEFAULT_KEY_PREFIX
    ) -> Awaitable[list[Any]] | list[Any]:
        return self.lrange(prefix + name, start, end)

    def prefixed_type(self, name: _KeyT, prefix: _KeyT = DEFAULT_KEY_PREFIX) -> ResponseT:
        return self.type(prefix + name)
