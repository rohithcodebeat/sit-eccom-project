from .serializers import ProductCategoryModelSerializer, ProductBrandModelSerializer, ProductColorModelSerializer, ProductDescriptionModelSerializer, ProductImageModelSerializer, ProductServiceModelSerializer, ProductVariationModelSerializer, ProductModelCreateSerializer, ProductModelListSerializer, DashboardProductMainModelCreateSerializer, DashboardProductMainListSerializer
from ..models import ProductCategoryModel, ProductBrandModel, ProductColorModel, ProductDescriptionModel, ProductImageModel, ProductServiceModel, ProductVariationModel, ProductModel, ProductMainModel
from rest_framework import generics, status, filters 
from rest_framework.response import Response  
import django_filters
from ..filters import ProductFilter, ProductMainModelFilter

class DasboardProductCategoryModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategoryModelSerializer


class DasboardProductCategoryModelGenericAPIView(generics.GenericAPIView):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategoryModelSerializer

    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(data=request.data, instance=queryset)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Category is Updated!"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id).delete()
            return Response({"messge" : "Category is deleted!"},stauts=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)



    

class DasboardProductBrandModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductBrandModel.objects.all()
    serializer_class = ProductBrandModelSerializer

class DasboardProductBrandModelGenericAPIView(generics.GenericAPIView):
    queryset = ProductBrandModel.objects.all()
    serializer_class = ProductBrandModelSerializer

    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(data=request.data, instance=queryset)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Brand is Updated!"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id).delete()
            return Response({"messge" : "Brand is deleted!"},stauts=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)



class DasboardProductColorModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorModelSerializer


class DasboardProductColorModelGenericAPIView(generics.ListCreateAPIView):
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorModelSerializer

    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(data=request.data, instance=queryset)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Color is Updated!"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id).delete()
            return Response({"messge" : "Color is deleted!"},stauts=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    



class DasboardProductDescriptionModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductDescriptionModel.objects.all()
    serializer_class = ProductDescriptionModelSerializer
    

class DasboardProductDescriptionModelGenericAPIView(generics.GenericAPIView):
    queryset = ProductDescriptionModel.objects.all()
    serializer_class = ProductDescriptionModelSerializer

    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(data=request.data, instance=queryset)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Description is Updated!"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id).delete()
            return Response({"messge" : "Description is deleted!"},stauts=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    

    


class DasboardProductImageModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageModelSerializer

class DasboardProductImageModelGenericAPIView(generics.GenericAPIView):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageModelSerializer

    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(data=request.data, instance=queryset)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Product Image is Updated!"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id).delete()
            return Response({"messge" : "Product Image is deleted!"},stauts=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    



    
class DasboardProductServiceModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductServiceModel.objects.all()
    serializer_class = ProductServiceModelSerializer


class DasboardProductServiceModelGenericAPIView(generics.GenericAPIView):
    queryset = ProductServiceModel.objects.all()
    serializer_class = ProductServiceModelSerializer

    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(data=request.data, instance=queryset)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Product Service is Updated!"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id).delete()
            return Response({"messge" : "Product Service is deleted!"},stauts=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)



class DasboardProductVariationModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductVariationModel.objects.all()
    serializer_class = ProductVariationModelSerializer

class DasboardProductVariationModelGenericAPIView(generics.GenericAPIView):
    queryset = ProductVariationModel.objects.all()
    serializer_class = ProductVariationModelSerializer


    def get(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            queryset = self.queryset.get(pk=id)
            serializer = self.serializer_class(data=request.data, instance=queryset)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Product Variation is Updated!"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            queryset = self.queryset.get(pk=id).delete()
            return Response({"messge" : "Product Variation is deleted!"},stauts=status.HTTP_200_OK)
        except:
            return Response({"messge" : "something went wrong!"},status=status.HTTP_400_BAD_REQUEST)    



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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ["title", "brand__title", "description__description", "category__title", "services__title", "variation__title", "color__title"]



class DashboardProductMainModelCreateAPIView(generics.CreateAPIView):
    queryset = ProductMainModel.objects.all()
    serializer_class = DashboardProductMainModelCreateSerializer


class DashboardProductMainModelListAPIView(generics.ListAPIView):
    queryset = ProductMainModel.objects.all()
    serializer_class = DashboardProductMainListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductMainModelFilter
    search_fields = ["product__title", "product__brand__title","product__description__description","product__category__title", "product__services__title","product__variation__title","product_code", "variation__title", "color__title", "price"]