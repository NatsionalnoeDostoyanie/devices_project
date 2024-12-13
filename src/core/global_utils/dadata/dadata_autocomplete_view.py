from django.conf import settings
from django.http import (
    HttpRequest,
    JsonResponse,
)

from core.global_utils.cache.custom_redis import CustomRedis
from core.global_utils.dadata.extensions.sync.client_singletons import SuggestClientSingleton


def dadata_autocomplete_view(request: HttpRequest) -> JsonResponse:
    if not (query := request.GET.get("q")):
        # Returning JsonResponse() with an empty tuple is a little faster than returning it with an empty list
        # (I've checked)
        return JsonResponse({"results": ()})

    def _fetch_results_from_api() -> tuple[str, ...]:
        results = tuple(
            item["unrestricted_value"]
            for item in SuggestClientSingleton(
                settings.DADATA_API_KEY, settings.DADATA_SECRET_KEY  # type: ignore[misc]
            ).suggest(name="address", query=query, count=5)
        )
        return results

    custom_redis = CustomRedis()
    cache_key = "dadata_address_autocomplete:" + query
    match custom_redis.prefixed_type(cache_key):
        case b"none":
            if len(data := _fetch_results_from_api()) > 1:
                custom_redis.prefixed_rpush(cache_key, *data)
            elif len(data) == 1:
                custom_redis.prefixed_setex(cache_key, *data)
        case b"list":
            data = tuple(
                map(
                    lambda item: item.decode("utf-8"),
                    custom_redis.prefixed_lrange(cache_key, 0, -1),  # type: ignore[arg-type]
                )
            )
        case b"string":
            data = (custom_redis.prefixed_get(cache_key).decode("utf-8"),)  # type: ignore[union-attr]
        case _:
            data = tuple()

    return JsonResponse(
        {
            "results": tuple(
                {
                    "id": text,
                    "text": text,
                }
                for text in data
            )
        }
    )
