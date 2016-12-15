from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


_DEFAULT_CONFERENCE = _NOT_SET = object()


class ConferenceManager(models.Manager):

    def get_default(self):
        """Get current default conference for filtering things in UI.

        This uses a setting to identify the current default conference, and
        caches the result to avoid subsequent database hit.
        """
        global _DEFAULT_CONFERENCE
        if _DEFAULT_CONFERENCE is not _NOT_SET:
            return _DEFAULT_CONFERENCE
        qs = self.get_queryset()
        _DEFAULT_CONFERENCE = qs.get(slug=settings.CONFERENCE_DEFAULT_SLUG)
        return _DEFAULT_CONFERENCE

    def clear_cache(self):
        global _DEFAULT_CONFERENCE
        _DEFAULT_CONFERENCE = _NOT_SET


class Conference(models.Model):

    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        unique=True,
    )

    objects = ConferenceManager()

    class Meta:
        verbose_name = _('conference')
        verbose_name_plural = _('conferences')
