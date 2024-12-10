from django.contrib.auth import get_user_model
from django.db.models import (
    SET_NULL,
    CharField,
    ForeignKey,
    GenericIPAddressField,
    Model,
    TextField,
)
from django.utils.translation import gettext_lazy as _

from devices_app.models.device_model import DeviceModel


class Device(Model):
    address = CharField(verbose_name=_("Address"), max_length=255, db_index=True)
    comment = TextField(verbose_name=_("Comment"), blank=True, null=True)
    ip_address = GenericIPAddressField(verbose_name=_("IP Address"), unique=True)
    name = CharField(verbose_name=_("Name"), max_length=255, db_index=True)

    author = ForeignKey(
        get_user_model(),
        on_delete=SET_NULL,
        related_name="devices",
        verbose_name=_("Author"),
        blank=True,
        null=True,
    )
    model = ForeignKey(
        DeviceModel, on_delete=SET_NULL, related_name="devices", verbose_name=_("Model"), blank=True, null=True
    )

    def __str__(self) -> str:
        return f"({self.ip_address}) {self.name}"
