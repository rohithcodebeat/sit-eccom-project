from products.dashboard.serializers import ProductModelListSerializer
from ..models import ProductModel
from ..filters import ProductFilter
from rest_framework import serializers, status, generics 
from rest_framework.response import Response
import django_filters

class WebsiteProductModelListAPIView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter


