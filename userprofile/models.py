from django.db import models
from django.contrib.auth import get_user_model
from products.models import ProductMainModel
# from orders.models import OrderModel
# Create your models here.

class UserAddressModel(models.Model):
    address_1 = models.CharField(max_length=100, null=True, blank=True)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserWishListModel(models.Model):
    products = models.ManyToManyField(ProductMainModel, related_name="UserWishListModel_products", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserCartModel(models.Model):
    products = models.ManyToManyField(ProductMainModel, related_name="UserCartModel_products",  blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


GENDER = [
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHERS", "OTHERS"),
]

class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="UserProfileModel_user", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    primary_number = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True, choices=GENDER)

    address = models.ManyToManyField(UserAddressModel, related_name="UserProfileModel_address", blank=True)
    wishlist = models.OneToOneField(UserWishListModel, on_delete=models.CASCADE,related_name="UserProfileModel_wishlist", blank=True, null=True)
    cart = models.OneToOneField(UserCartModel, on_delete=models.CASCADE,related_name="UserProfileModel_cart", blank=True, null=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




