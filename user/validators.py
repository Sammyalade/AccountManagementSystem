from django.core.exceptions import ValidationError


def validate_phone(phone):
    if len(phone) != 11:
        raise ValidationError('Phone number must be 11 digits')
