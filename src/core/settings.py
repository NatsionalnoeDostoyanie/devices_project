import django_stubs_ext
from split_settings.tools import include


django_stubs_ext.monkeypatch()

include("../settings/*.py")
