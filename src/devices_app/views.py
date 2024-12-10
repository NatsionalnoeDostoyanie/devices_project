from rest_framework.viewsets import ModelViewSet

from devices_app.models.device import Device
from devices_app.models.device_model import DeviceModel
from devices_app.serializers import (
    DeviceModelSerializer,
    DeviceSerializer,
)


class DeviceViewSet(ModelViewSet[Device]):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DeviceModelViewSet(ModelViewSet[DeviceModel]):
    serializer_class = DeviceModelSerializer
    queryset = DeviceModel.objects.all()
