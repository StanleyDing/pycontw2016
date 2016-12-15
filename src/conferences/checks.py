from django.apps import apps
from django.core import checks


def default_conference_check(app_configs, **kwargs):
    """Make sure there is a valid default conference.
    """
    errors = []

    model = None
    if app_configs is None:
        model = apps.get_model('conferences.Conference')
    else:
        for app_config in app_configs:
            if app_config.label == 'conferences':
                model = app_config.get_model('Conference')
                break

    if model is not None:
        try:
            model.objects.get_default()
        except model.DoesNotExist:
            errors.append(
                checks.Error(
                    'invalid default conference',
                    hint=(
                        'Default conference Does not exist. Check your '
                        'CONFERENCE_DEFAULT_SLUG setting, and make sure a '
                        'conference with matching slug exists.'
                    ),
                    id='conferences.E001',
                )
            )
    return errors
