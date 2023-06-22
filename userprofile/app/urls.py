from django.urls import path 
from .views import AppUserWishListUpdateAPIView, AppUserWishListRemoveAPIView, AppUserWishListAPIView, AppUserCartListUpdateAPIView, AppUserCartListRemoveAPIView, AppUserCartListAPIView, AppUserProfileModelUpdateAPIView

urlpatterns = [
    path("add-to-wishlist/", AppUserWishListUpdateAPIView.as_view(), name="AppUserWishListUpdateAPIView"),
    path("remove-to-wishlist/", AppUserWishListRemoveAPIView.as_view(), name="AppUserWishListRemoveAPIView"),
    path("user-wishlist/", AppUserWishListAPIView.as_view(), name="AppUserWishListAPIView"),
    path("add-to-cart/", AppUserCartListUpdateAPIView.as_view(), name="AppUserCartListUpdateAPIView"),
    path("remove-to-cart/", AppUserCartListRemoveAPIView.as_view(), name="AppUserCartListRemoveAPIView"),
    path("user-cart/", AppUserCartListAPIView.as_view(), name="AppUserCartListAPIView"),    
    path("user-profile/", AppUserProfileModelUpdateAPIView.as_view(), name="AppUserProfileModelUpdateAPIView"),
]


