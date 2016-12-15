from django.apps import AppConfig as BaseAppConfig
from django.core import checks
from django.utils.translation import ugettext_lazy as _

from .checks import default_conference_check


class AppConfig(BaseAppConfig):

    name = 'conferences'
    verbose_name = _('Conferences')

    def ready(self):
        checks.register(default_conference_check, checks.Tags.models)
