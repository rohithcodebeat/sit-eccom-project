from ..models import OrderModel, PaymentDetailModel
from rest_framework import serializers 
from userprofile.app.serializers import AppUserAddressModelListSerializer
from datetime import datetime 



class WebsiteOrderModelCreateSerializer(serializers.ModelSerializer):
    payment_mode = serializers.CharField(max_length=100)
    transcation_id = serializers.CharField(max_length=100)

    class Meta:
        model = OrderModel 
        exclude = ("status", "date_of_delivery", "user", "date_of_order", "payment_details")
    
    def validate(self, data):
        if data["product"].is_ordered:
            raise serializers.ValidationError({"message" : "Product is Sold"})
        return data 
        

    def create(self, validated_data):
        # print(validated_data)
        # payment_mode = validated_data.pop("payment_mode")
        # transcation_id = validated_data.pop("transcation_id")
        product = validated_data["product"]
        shipping_fee = 0
        final_price = product.price - product.discount + shipping_fee
        instance = PaymentDetailModel.objects.create(
            transcation_id=validated_data.pop("transcation_id"),
            payment_mode=validated_data.pop("payment_mode"),
            actual_price=product.price,
            discount_price=product.discount, 
            final_price=final_price, 
            shipping_fee=0)
        OrderModel.objects.create(
            payment_details=instance,
            user=self.context["request"].user,
            date_of_order=datetime.now(),
            order_id=validated_data["order_id"], 
            address=validated_data["address"], 
            product=product)
        product.is_ordered = True 
        product.save()
        return validated_data


class WebsiteOrderModelListSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = "__all__"

    def get_address(self, obj):
        try:
            data = AppUserAddressModelListSerializer(obj.address, many=False).data 
        except:
            data = {}
        return data 