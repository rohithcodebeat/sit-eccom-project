from rest_framework import serializers
from ..models import UserWishListModel, UserCartModel, UserProfileModel, UserAddressModel
from products.dashboard.serializers import DashboardProductMainListSerializer



class AppUserWishListUpdateSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField()
    class Meta:
        model = UserWishListModel
        fields =  ["product_code"]


class AppUserCartListUpdateSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField()
    class Meta:
        model = UserCartModel
        fields =  ["product_code"]
    

class AppUserWishListSerializer(serializers.ModelSerializer):
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
    


class AppUserCartListSerializer(serializers.ModelSerializer):
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


class AppUserAddressModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddressModel 
        fields = "__all__"

class AppUserProfileModelUpdateSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    class Meta:
        model = UserProfileModel 
        exclude = ["wishlist", "cart", "user"]

    def get_address(self, obj):
        try:
            data = AppUserAddressModelListSerializer(obj.address.all(), many=True).data
        except:
            data = []
        return data 

class AppUserAddressModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddressModel 
        fields = "__all__"


class AppUserAddressModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddressModel 
        fields = "__all__"
    

    def create(self, validated_data): 
        address_instance =  UserAddressModel.objects.create(**validated_data)
        instance  = UserProfileModel.objects.get(user=self.context["request"].user) 
        instance.address.add(address_instance)
        instance.save()
        return validated_data 


class AppUserAddressModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddressModel 
        fields = "__all__"
