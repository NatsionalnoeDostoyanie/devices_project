import contextlib
from typing import (
    Any,
    TypeVar,
    cast,
)

from django.conf import settings
from django.db.models import Model
from django.db.models.query import QuerySet
from rest_framework.pagination import (
    LimitOffsetPagination,
    _positive_int,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


_MT = TypeVar("_MT", bound=Model)


class CustomLimitOffsetPagination(LimitOffsetPagination):
    # TODO: Consider removing `cast()` since `settings.DB_MAX_INT` is guaranteed to exist and is `int`
    # (used for type checking)
    default_limit = cast(int, settings.DB_MAX_INT)  # type: ignore[misc]

    def get_limit(self, request: Request) -> int:
        if self.limit_query_param:
            with contextlib.suppress(KeyError, ValueError):
                return _positive_int(request.query_params[self.limit_query_param], cutoff=self.max_limit)
        return self.default_limit

    def paginate_queryset(self, queryset: QuerySet[_MT], request: Request, view: APIView | None = None) -> list[_MT]:
        self.request = request
        self.limit = self.get_limit(request)
        self.offset = self.get_offset(request)
        self.total = queryset.count()
        self.results_count = (results := queryset[self.offset : self.offset + self.limit]).count()
        return list(results)

    def get_paginated_response(self, data: Any) -> Response:
        return Response(
            {
                "meta": {
                    "results_count": self.results_count,
                    "total": self.total,
                },
                "results": data,
            }
        )
