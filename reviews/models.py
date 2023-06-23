from django.db import models
from django.contrib.auth import get_user_model 
from products.models import ProductModel
# Create your models here.

class ProductReviewImageModel(models.Model):
    image = models.FileField(upload_to="product-review-image/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductReviewModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="ProductReviewModel_user")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="ProductReviewModel_product")

    title = models.CharField(max_length=200, null=True, blank=True) #
    image = models.ManyToManyField(ProductReviewImageModel, related_name="ProductReviewModel_image", blank=True)
    description = models.TextField(blank=True, null=True)
    ratings = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



