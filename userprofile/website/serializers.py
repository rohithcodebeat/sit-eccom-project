from rest_framework import serializers
from ..models import UserWishListModel, UserCartModel, UserProfileModel, UserAddressModel
from products.dashboard.serializers import DashboardProductMainListSerializer



class WebsiteUserWishListUpdateSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField()
    class Meta:
        model = UserWishListModel
        fields =  ["product_code"]


class WebsiteUserCartListUpdateSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField()
    class Meta:
        model = UserCartModel
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
    


class WebsiteUserCartListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = UserCartModel 
        fields = "__all__"

    def get_products(self, obj):
        try:
            data = DashboardProductMainListSerializer(obj.products.all(), many=True).data 
        except:
            data = []
        return data  


class WebsiteUserAddressModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddressModel 
        fields = "__all__"

class WebsiteUserProfileModelUpdateSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    class Meta:
        model = UserProfileModel 
        exclude = ["wishlist", "cart", "user"]

    def get_address(self, obj):
        try:
            data = WebsiteUserAddressModelListSerializer(obj.address.all(), many=True).data
        except:
            data = []
        return data 
