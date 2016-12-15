from django.core import checks


def default_conference_check(app_configs, **kwargs):
    """Make sure there is a valid default conference.
    """
    errors = []

    for app_config in app_configs:
        if app_config.label == 'conferences':
            Conference = app_config.get_model('Conference')
            break

    try:
        Conference.objects.get_default()
    except Conference.DoesNotExist:
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
