import os

from rest_framework import serializers

from .models import Product
from .services import convert_image


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'sku',
            'price',
            'status',
            'image',
        ]

    def get_image(self, instance):
        file_name, ext = os.path.splitext(instance.image.url)
        convert_image(instance)
        return {
            'path': file_name,
            'formats': [ext.replace('.', ''), 'webp']
        }
