from django.core.exceptions import ValidationError
import re

def only_letters_spaces(value):
    if not re.match(r"^[A-Za-z' ]+$", value):
        raise ValidationError('Name may contain only letters and spaces.')
