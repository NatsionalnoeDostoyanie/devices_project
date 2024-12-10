from django.contrib import admin
from django.urls import (
    include,
    path,
)
from rest_framework.authtoken.views import obtain_auth_token

from core.global_utils.dadata.dadata_autocomplete_view import dadata_autocomplete_view


urlpatterns = (
    path("admin/", admin.site.urls),
    path("api/v1/devices/", include("devices_app.urls")),
    path("api/v1/token/", obtain_auth_token),
    path("autocomplete/dadata/", dadata_autocomplete_view, name="dadata_autocomplete"),
)
