from ..models import ProductCategoryModel, ProductBrandModel, ProductColorModel, ProductDescriptionModel, ProductImageModel, ProductServiceModel, ProductVariationModel, ProductModel, ProductMainModel
from rest_framework import serializers

class ProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = "__all__"


class ProductBrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrandModel
        fields = "__all__"


class ProductColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColorModel
        fields = "__all__"


class ProductDescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescriptionModel
        fields = "__all__"

class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = "__all__"


class ProductServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductServiceModel
        fields = "__all__"


class ProductVariationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariationModel
        fields = "__all__"

class ProductModelListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    variation = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = "__all__"
    
    def get_category(self, obj):
        try:
            data = ProductCategoryModelSerializer(obj.category, many=False).data
        except:
            data = {}
        return data

    def get_brand(self, obj):
        try:
            data = ProductBrandModelSerializer(obj.brand, many=False).data
        except:
            data = {}
        return data 


    def get_services(self, obj):
        try:
            data = ProductServiceModelSerializer(obj.services.all(), many=True).data 
        except Exception as e:

            data = [str(e)]
        return data 
    
    def get_description(self, obj):
        try:
            data = ProductDescriptionModelSerializer(obj.description.all(), many=True).data 
        except:
            data = []
        return data 
    
    def get_images(self, obj):
        try:
            data = ProductImageModelSerializer(obj.images.all(), many=True).data
        except:
            data = []
        return data 
    
    def get_variation(self, obj):
        try:
            data = ProductVariationModelSerializer(obj.variation.all(), many=True).data
        except:
            data = []
        return data 
    
    def get_color(self, obj):
        try:
            data = ProductColorModelSerializer(obj.color.all(), many=True).data 
        except:
            data = []
        return data 
    
    
    

class ProductModelCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    description = serializers.ListField()
    class Meta:
        model = ProductModel 
        exclude = ("images",)
    

    def create(self, validated_data):
        req_image = self.context["request"].data.getlist('image')
        req_descripiton = self.context["request"].data.getlist('description')
        
        images = validated_data.pop('image')
        # dummy_images = validated_data.pop('images')
        
        descripiton = validated_data.pop("description")

        # instances
        services = validated_data.pop("services")
        color = validated_data.pop("color")
        variation = validated_data.pop("variation")
        
        # print(validated_data)
        instance = ProductModel.objects.create(**validated_data)

        instance.services.set(services)
        instance.color.set(color)
        instance.variation.set(variation)

        for img in req_image:
            mediainstance = ProductImageModel.objects.create(image=img)    
            instance.images.add(mediainstance)
        
        for data in req_descripiton:
            description_instance = ProductDescriptionModel.objects.create(description=data)
            instance.description.add(description_instance)



        return validated_data
    

class DashboardProductMainModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMainModel 
        fields = "__all__"


class DashboardProductMainListSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    variation = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    class Meta:
        model = ProductMainModel 
        fields = "__all__"

    
    def get_variation(self, obj):
        try:
            data = ProductVariationModelSerializer(obj.variation, many=False).data
        except:
            data = {}
        return data 
    
    def get_color(self, obj):
        try:
            data = ProductColorModelSerializer(obj.color, many=False).data 
        except:
            data = {}
        return data 


    def get_product(self, obj):
        try:
            data = ProductModelListSerializer(obj.product, many=False).data 
        except:
            data = {}
        return data