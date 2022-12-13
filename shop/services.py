import os

from PIL import Image


def convert_image(instance):
    image_path = instance.image.path
    image_name, file_ext = os.path.splitext(image_path)
    img = Image.open(image_path).convert('RGB')
    img.save(f'{image_name}.webp', 'WEBP')
