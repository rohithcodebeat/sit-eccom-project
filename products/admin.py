from django.contrib import admin
from .models import ProductCategoryModel, ProductBrandModel, ProductColorModel, ProductDescriptionModel, ProductImageModel, ProductServiceModel, ProductVariationModel, ProductModel, ProductMainModel
# Register your models here.

admin.site.register(ProductCategoryModel)
admin.site.register(ProductBrandModel)
admin.site.register(ProductColorModel)
admin.site.register(ProductDescriptionModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductServiceModel)
admin.site.register(ProductVariationModel)
admin.site.register(ProductModel)
admin.site.register(ProductMainModel)
