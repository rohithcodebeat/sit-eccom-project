from ..models import ProductReviewModel, ProductReviewImageModel
from orders.models import OrderModel
from products.models import ProductMainModel, ProductModel
from rest_framework import serializers 

class WebsiteProductReviewModelCreateSerializer(serializers.ModelSerializer):
    images = serializers.ImageField(required=False)
    class Meta:
        model = ProductReviewModel
        # fields = "__all__"
        exclude = ("user", "image",)

    def validate(self, data):
        product = data["product"]
        if not OrderModel.objects.filter(user=self.context["request"].user, product__product=product).exists():
            raise serializers.ValidationError({"message" : "You can only review the project after ordering"})


        return data

    def create(self, validated_data): 
        images = self.context["request"].data.getlist("images")
        validated_data.pop("images")
        instance = ProductReviewModel.objects.create(user=self.context["request"].user, **validated_data)
        for img in images:
            img_instance = ProductReviewImageModel.objects.create(image=img)
            instance.image.add(img_instance)
            instance.save()

        return validated_data 

