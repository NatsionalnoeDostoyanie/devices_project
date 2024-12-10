from dal.autocomplete import ListSelect2
from django.forms import (
    CharField,
    ModelForm,
)

from devices_app.models.device import Device


class DeviceAdminForm(ModelForm[Device]):
    address = CharField(max_length=255, widget=ListSelect2(url="dadata_autocomplete"))
