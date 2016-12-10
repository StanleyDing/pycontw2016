from django.db import models
from django.utils.translation import ugettext_lazy as _


class Conference(models.Model):

    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
    )

    class Meta:
        verbose_name = _('conference')
        verbose_name_plural = _('conferences')
