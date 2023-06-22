from products.dashboard.serializers import ProductModelListSerializer
from ..models import ProductModel
from rest_framework import serializers, status, generics, filters 
from rest_framework.response import Response
import django_filters
from ..filters import ProductFilter


class AppProductModelListAPIView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ["title", "brand__title", "description__description", "category__title", "services__title", "variation__title", "color__title"]


