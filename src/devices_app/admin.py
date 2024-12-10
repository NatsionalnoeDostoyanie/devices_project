from django.contrib.admin import (
    ModelAdmin,
    register,
)
from django.utils.translation import gettext_lazy as _

from devices_app.forms import DeviceAdminForm
from devices_app.models.device import Device
from devices_app.models.device_model import DeviceModel


@register(Device)
class DeviceAdmin(ModelAdmin[Device]):
    form = DeviceAdminForm
    list_display = ("__str__", "address", "comment")
    fieldsets = (
        (_("Base data"), {"fields": ("address", "name", "ip_address", "comment")}),
        (_("Related data"), {"fields": ("model", "author")}),
    )


@register(DeviceModel)
class DeviceModelAdmin(ModelAdmin[DeviceModel]):
    list_display = ("name", "description")
    fields = ("name", "description")
