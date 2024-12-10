from django.urls import (
    include,
    path,
)
from rest_framework.routers import DefaultRouter

from devices_app.views import (
    DeviceModelViewSet,
    DeviceViewSet,
)


router = DefaultRouter()
router.register("devices", DeviceViewSet)
router.register("device-models", DeviceModelViewSet)

urlpatterns = (path("", include(router.urls)),)
