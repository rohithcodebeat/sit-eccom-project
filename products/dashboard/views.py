from .serializers import ProductCategoryModelSerializer, ProductBrandModelSerializer, ProductColorModelSerializer, ProductDescriptionModelSerializer, ProductImageModelSerializer, ProductServiceModelSerializer, ProductVariationModelSerializer, ProductModelCreateSerializer, ProductModelListSerializer
from ..models import ProductCategoryModel, ProductBrandModel, ProductColorModel, ProductDescriptionModel, ProductImageModel, ProductServiceModel, ProductVariationModel, ProductModel, ProductMainModel
from rest_framework import generics, status
from rest_framework.response import Response  

class DasboardProductCategoryModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategoryModelSerializer
    

class DasboardProductBrandModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductBrandModel.objects.all()
    serializer_class = ProductBrandModelSerializer
    
class DasboardProductColorModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorModelSerializer
    
class DasboardProductDescriptionModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductDescriptionModel.objects.all()
    serializer_class = ProductDescriptionModelSerializer
    
class DasboardProductImageModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageModelSerializer
    
class DasboardProductServiceModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductServiceModel.objects.all()
    serializer_class = ProductServiceModelSerializer
    
class DasboardProductVariationModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductVariationModel.objects.all()
    serializer_class = ProductVariationModelSerializer
    

class DashboardProductModelCreateAPIView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelCreateSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={"request" : request}) 
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Product is created"}, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DasboardProductModelListAPIView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelListSerializer

