from django.db import models

# Create your models here.
class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductBrandModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductColorModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductDescriptionModel(models.Model):
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductImageModel(models.Model):
    image = models.FileField(upload_to="product-image/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductServiceModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    icon = models.FileField(upload_to="product-image/services/", null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ProductVariationModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, related_name="ProductVariationModel_category", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



class ProductModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    brand = models.ForeignKey(ProductBrandModel, on_delete=models.CASCADE, related_name="ProductModel_brand", null=True, blank=True)
    images = models.ManyToManyField(ProductImageModel, related_name="ProductModel_images",blank=True)
    description = models.ManyToManyField(ProductDescriptionModel, related_name="ProductModel_description", blank=True)
    category = models.ForeignKey(ProductCategoryModel, related_name="ProductModel_category", on_delete=models.CASCADE, null=True, blank=True)
    services = models.ManyToManyField(ProductServiceModel, related_name="ProductModel_services", blank=True)
    variation = models.ManyToManyField(ProductVariationModel, related_name="ProductModel_variation", blank=True)
    color = models.ManyToManyField(ProductColorModel, related_name="ProductModel_color", blank=True)

    
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



class ProductMainModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="ProductMainModel_product", null=True, blank=True)

    product_code = models.CharField(max_length=100, unique=True, primary_key=True)

    variation = models.ForeignKey(ProductVariationModel, on_delete=models.CASCADE, related_name="ProductMainModel_variation", null=True, blank=True)

    color = models.ForeignKey(ProductColorModel, on_delete=models.CASCADE, related_name="ProductMainModel_color", null=True, blank=True)

    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    final_price = models.DecimalField(decimal_places=2, max_digits=10)

    is_ordered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
https://www.amazon.in/Amazon-Brand-Solimo-Filled-Beans/dp/B08GS5CLSS/?_encoding=UTF8&pd_rd_w=kjsG7&content-id=amzn1.sym.22a42d01-0089-4fec-a28b-ec7a361d085f&pf_rd_p=22a42d01-0089-4fec-a28b-ec7a361d085f&pf_rd_r=CTY293CFE9678A2WYVFF&pd_rd_wg=7iIsN&pd_rd_r=fd258e28-f4e5-4ccc-b2d8-05728c2f7d9e&ref_=pd_gw_ci_mcx_mr_hp_d&th=1
https://www.amazon.in/Amazon-Brand-Solimo-Filled-Beans/dp/B08GRSBWQH/?_encoding=UTF8&pd_rd_w=kjsG7&content-id=amzn1.sym.22a42d01-0089-4fec-a28b-ec7a361d085f&pf_rd_p=22a42d01-0089-4fec-a28b-ec7a361d085f&pf_rd_r=CTY293CFE9678A2WYVFF&pd_rd_wg=7iIsN&pd_rd_r=fd258e28-f4e5-4ccc-b2d8-05728c2f7d9e&ref_=pd_gw_ci_mcx_mr_hp_d&th=1
https://amzn.eu/d/9ivLckR
https://amzn.eu/d/b5KJAp9
"""
