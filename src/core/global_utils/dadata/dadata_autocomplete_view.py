from django.conf import settings
from django.core.cache import cache
from django.http import (
    HttpRequest,
    JsonResponse,
)

from core.global_utils.dadata.extensions.sync.client_singletons import SuggestClientSingleton


def dadata_autocomplete_view(request: HttpRequest) -> JsonResponse:
    if not (query := request.GET.get("q")):
        return JsonResponse({"results": []})

    def _fetch_and_cache_results_from_api() -> tuple[str, ...]:
        results = tuple(
            item["unrestricted_value"]
            for item in SuggestClientSingleton(
                settings.DADATA_API_KEY, settings.DADATA_SECRET_KEY  # type: ignore[misc]
            ).suggest(name="address", query=query, count=5)
        )
        if results:
            cache.set(prefixed_cache_key, results)
        return results

    prefixed_cache_key = "dadata_address_autocomplete__" + query
    return JsonResponse(
        {
            "results": tuple(
                {"id": text, "text": text}
                for text in cache.get(prefixed_cache_key, _fetch_and_cache_results_from_api())
            )
        }
    )
