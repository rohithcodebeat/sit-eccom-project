from rest_framework import serializers
from ..models import UserWishListModel 
from products.dashboard.serializers import DashboardProductMainListSerializer



class WebsiteUserWishListUpdateSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField()
    class Meta:
        model = UserWishListModel
        fields =  ["product_code"]
    

class WebsiteUserWishListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = UserWishListModel 
        fields = "__all__"

    def get_products(self, obj):
        try:
            data = DashboardProductMainListSerializer(obj.products.all(), many=True).data 
        except:
            data = []
        return data  

