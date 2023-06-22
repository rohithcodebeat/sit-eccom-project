from .serializers import DashboardUserWishListSerializer, DashboardUserCartListSerializer
from ..models import UserWishListModel, UserCartModel
from rest_framework import generics, status 
from rest_framework.response import Response 



class DasboardUserCartListAPIView(generics.ListAPIView):
    queryset = UserCartModel.objects.all()
    serializer_class = DashboardUserCartListSerializer

    

class DashboardUserWishListAPIView(generics.ListAPIView):
    queryset = UserWishListModel.objects.all()
    serializer_class = DashboardUserWishListSerializer

