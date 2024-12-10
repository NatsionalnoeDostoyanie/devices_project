from dadata import Dadata
from dadata.sync import (
    CleanClient,
    ClientBase,
    ProfileClient,
    SuggestClient,
)

from core.global_utils.base_singlton_mixin import BaseSingletonMixin


# fmt: off
class ClientBaseSingleton(BaseSingletonMixin, ClientBase):        # type: ignore[misc]
    """
    Base class for API client (Singleton).
    """


class CleanClientSingleton(BaseSingletonMixin, CleanClient):      # type: ignore[misc]
    """
    Dadata Cleaner API client (Singleton).
    """


class SuggestClientSingleton(BaseSingletonMixin, SuggestClient):  # type: ignore[misc]
    """
    Dadata Suggestions API client (Singleton).
    """


class ProfileClientSingleton(BaseSingletonMixin, ProfileClient):  # type: ignore[misc]
    """
    Dadata Profile API client (Singleton).
    """


class DadataSingleton(BaseSingletonMixin, Dadata):                # type: ignore[misc]
    """
    Synchronous Dadata API client (Singleton).
    """


# fmt: on
