from rest_framework.serializers import ModelSerializer

from devices_app.models.device import Device
from devices_app.models.device_model import DeviceModel


class DeviceModelSerializer(ModelSerializer[DeviceModel]):
    class Meta:
        model = DeviceModel
        fields = ("id", "name", "description")


class DeviceSerializer(ModelSerializer[Device]):
    model = DeviceModelSerializer(read_only=True)

    class Meta:
        model = Device
        fields = ("id", "address", "name", "ip_address", "comment", "model", "author")
