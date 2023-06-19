from django.contrib import admin
from .models import UserAddressModel, UserWishListModel, UserCartModel, UserProfileModel
# Register your models here.
admin.site.register(UserAddressModel)
admin.site.register(UserWishListModel)
admin.site.register(UserCartModel)
admin.site.register(UserProfileModel)

