from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = 'status',
    search_fields = 'title', 'sku',
