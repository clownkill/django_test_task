import os

from django.core.exceptions import ValidationError


def image_extension_validator(image):
    _, img_extension = os.path.splitext(image.name)
    if img_extension.lower() not in ('.png', '.jpg', '.jpeg'):
        raise ValidationError(
            message='Неподдерживаемый формат изображения '
                    '(Ожидалось: .png, .jpg, .jpeg)'
        )
    return True