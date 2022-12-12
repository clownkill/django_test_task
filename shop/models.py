import os

from django.db import models
from django.core.validators import MinValueValidator
from PIL import Image

from .validators import image_extension_validator


def generate_path(instance, filename):
    return os.path.join('images', instance.title, filename)


class Product(models.Model):
    STATUS_CHOICES = [
        ('STOCK', 'В наличии'),
        ('ORDER', 'Под заказ'),
        ('EXPECTED', 'Ожидается поступление'),
        ('OUT', 'Нет в наличии'),
        ('NOT PRODUCED', 'Не производится'),
    ]

    title = models.CharField('Название', max_length=255)
    sku = models.CharField('Артикул', max_length=255, unique=True)
    price = models.DecimalField(
        'Цена',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0),]
    )
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Изображение',
        upload_to= generate_path,
        validators=[image_extension_validator,],
        null=True,
        blank=True,
    )

    class Meta:
        ordering = 'title',
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        image_path = self.image.path
        file_name, ext = os.path.splitext(image_path)
        img = Image.open(image_path).convert('RGB')
        img.save(f'{file_name}.webp', 'WEBP')
