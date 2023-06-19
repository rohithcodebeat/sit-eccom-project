from django.contrib import admin
from .models import  PaymentDetailModel, OrderModel

# Register your models here.


admin.site.register(PaymentDetailModel)
admin.site.register(OrderModel)