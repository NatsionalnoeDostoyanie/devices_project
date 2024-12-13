from redis import Redis

from core.global_utils.base_singlton_mixin import BaseSingletonMixin


class RedisSingleton(BaseSingletonMixin, Redis):
    pass
