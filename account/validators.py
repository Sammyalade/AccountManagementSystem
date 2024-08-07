from django.core.exceptions import ValidationError


def validate_pin(pin):
    if len(pin) != 4:
        raise ValidationError('Pin must be 4 digits')


def validate_phone(phone):
    if len(phone) != 11:
        raise ValidationError('Phone number must be 11 digits')
