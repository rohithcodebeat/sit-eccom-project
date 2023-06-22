from ..models import UserWishListModel, UserProfileModel, UserCartModel
from products.models import  ProductMainModel, ProductModel
from .serializers import WebsiteUserWishListUpdateSerializer, WebsiteUserWishListSerializer, WebsiteUserCartListUpdateSerializer, WebsiteUserCartListSerializer, WebsiteUserProfileModelUpdateSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response 


class WebsiteUserWishListUpdateAPIView(generics.GenericAPIView):
    queryset = UserWishListModel.objects.all()
    serializer_class = WebsiteUserWishListUpdateSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        userprofile_query = UserProfileModel.objects.get(user=request.user)
        query = userprofile_query.wishlist 
        product = ProductMainModel.objects.get(product_code=request.data["product_code"])
        query.products.add(product)
        query.save()
        return Response({"message" : "Added to Wishlist"}, status=status.HTTP_200_OK)
    
    
class WebsiteUserWishListRemoveAPIView(generics.GenericAPIView):
    queryset = UserWishListModel.objects.all()
    serializer_class = WebsiteUserWishListUpdateSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        userprofile_query = UserProfileModel.objects.get(user=request.user)
        query = userprofile_query.wishlist 
        product = ProductMainModel.objects.get(product_code=request.data["product_code"])
        query.products.remove(product)
        query.save()
        return Response({"message" : "Removed to Wishlist"}, status=status.HTTP_200_OK)
    



class WebsiteUserWishListAPIView(generics.ListAPIView):
    queryset = UserWishListModel.objects.all()
    serializer_class = WebsiteUserWishListSerializer

    def get_queryset(self):
        return UserProfileModel.objects.get(user=self.request.user).wishlist 

    def list(self, request):
        serializer  = self.serializer_class(self.get_queryset(), many=False) 
        return Response(serializer.data, status=status.HTTP_200_OK)



class WebsiteUserCartListUpdateAPIView(generics.GenericAPIView):
    queryset = UserCartModel.objects.all()
    serializer_class = WebsiteUserCartListUpdateSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        userprofile_query = UserProfileModel.objects.get(user=request.user)
        query = userprofile_query.cart 
        product = ProductMainModel.objects.get(product_code=request.data["product_code"])
        query.products.add(product)
        query.save()
        return Response({"message" : "Added to Cart"}, status=status.HTTP_200_OK)
    
    
class WebsiteUserCartListRemoveAPIView(generics.GenericAPIView):
    queryset = UserCartModel.objects.all()
    serializer_class = WebsiteUserCartListUpdateSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        userprofile_query = UserProfileModel.objects.get(user=request.user)
        query = userprofile_query.cart 
        product = ProductMainModel.objects.get(product_code=request.data["product_code"])
        query.products.remove(product)
        query.save()
        return Response({"message" : "Removed to Cart"}, status=status.HTTP_200_OK)
    


class WebsiteUserCartListAPIView(generics.ListAPIView):
    queryset = UserCartModel.objects.all()
    serializer_class = WebsiteUserCartListSerializer

    def get_queryset(self):
        return UserProfileModel.objects.get(user=self.request.user).cart 

    def list(self, request):
        serializer  = self.serializer_class(self.get_queryset(), many=False) 
        return Response(serializer.data, status=status.HTTP_200_OK)


class WebsiteUserProfileModelUpdateAPIView(generics.GenericAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = WebsiteUserProfileModelUpdateSerializer

    def get(self, request):
        queryset = self.queryset.get(user=request.user)
        serializer = self.serializer_class(queryset, many=False) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        queryset = self.queryset.get(user=request.user)
        serializer = self.serializer_class(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    