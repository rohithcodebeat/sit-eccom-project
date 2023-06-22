import django_filters
from .models import ProductModel, ProductMainModel

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = ProductModel
        fields = ['brand', 'category', 'services', 'variation', 'color']


class ProductMainModelFilter(django_filters.FilterSet):
    class Meta:
        model = ProductMainModel
        fields = ['product' , 'variation', 'color']