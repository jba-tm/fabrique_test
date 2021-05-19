from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = 'fabrique_test.apps.core'
    label = 'app_core'
    verbose_name = _('core')
