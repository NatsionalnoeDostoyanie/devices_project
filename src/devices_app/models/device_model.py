from django.db.models import (
    CharField,
    Model,
    TextField,
)
from django.utils.translation import gettext_lazy as _


class DeviceModel(Model):
    description = TextField(verbose_name=_("Description"))
    name = CharField(verbose_name=_("Name"), max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.name
