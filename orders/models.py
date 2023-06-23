from django.db import models
from products.models import ProductMainModel
from django.contrib.auth import get_user_model
from userprofile.models import UserAddressModel
# Create your models here.

STATUS = [
    ("PENDING", "PENDING"),
    ("INPROGRESS" , "INPROGRESS"),
    ("DECLINED", "DECLINED"),
    ("CANCELED", "CANCELED"),
    ("COMPLETED", "COMPLETED"),
    ("SHIPPED", "SHIPPED"),
    ("DISPATCHED", "DISPATCHED"),
    ("OUT_FOR_DELIVERY", "OUT_FOR_DELIVERY")
]

PAYMENT = [
    ("CASH_ON_DELIVERY", "CASH_ON_DELIVERY"),
    ("DEBIT/CREDIT_CART", "DEBIT/CREDIT_CART"),
    ("UPI", "UPI")
]

class PaymentDetailModel(models.Model):
    transcation_id = models.CharField(max_length=100, unique=True, primary_key=True)
    actual_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    discount_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    final_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    shipping_fee = models.DecimalField(decimal_places=2, max_digits=10, default=0)


    discount_code = models.CharField(max_length=100, null=True, blank=True)
    payment_mode = models.CharField(max_length=100, null=True, blank=True, choices=PAYMENT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='OrderModel_user')
    order_id = models.CharField(max_length=100, unique=True, primary_key=True)
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE, related_name='OrderModel_product')
    status = models.CharField(max_length=50, blank=True, choices=STATUS, default="INPROGRESS")
    address = models.ForeignKey(UserAddressModel, on_delete=models.CASCADE, related_name='OrderModel_address', null=True, blank=True)
    payment_details = models.ForeignKey(PaymentDetailModel, on_delete=models.CASCADE, related_name="OrderModel_payment_details", null=True, blank=True)

    date_of_order = models.DateTimeField(null=True, blank=True)
    date_of_delivery = models.DateTimeField(null=True, blank=True)



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


