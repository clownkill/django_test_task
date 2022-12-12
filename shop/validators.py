import os

from django.core.exceptions import ValidationError


def image_extension_validator(image):
    _, img_extension = os.path.splitext(image.name)
    if img_extension.lower() not in ('.bmp', '.jpg', '.jpeg'):
        raise ValidationError
    return True