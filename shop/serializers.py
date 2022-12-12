import os

from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

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
        return {
            'path': file_name,
            'formats': [ext.replace('.',''), 'webp']
        }