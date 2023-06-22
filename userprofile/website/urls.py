from django.urls import path 
from .views import WebsiteUserWishListUpdateAPIView, WebsiteUserWishListRemoveAPIView, WebsiteUserWishListAPIView, WebsiteUserCartListUpdateAPIView, WebsiteUserCartListRemoveAPIView, WebsiteUserCartListAPIView, WebsiteUserProfileModelUpdateAPIView

urlpatterns = [
    path("add-to-wishlist/", WebsiteUserWishListUpdateAPIView.as_view(), name="WebsiteUserWishListUpdateAPIView"),
    path("remove-to-wishlist/", WebsiteUserWishListRemoveAPIView.as_view(), name="WebsiteUserWishListRemoveAPIView"),
    path("user-wishlist/", WebsiteUserWishListAPIView.as_view(), name="WebsiteUserWishListAPIView"),
    path("add-to-cart/", WebsiteUserCartListUpdateAPIView.as_view(), name="WebsiteUserCartListUpdateAPIView"),
    path("remove-to-cart/", WebsiteUserCartListRemoveAPIView.as_view(), name="WebsiteUserCartListRemoveAPIView"),
    path("user-cart/", WebsiteUserCartListAPIView.as_view(), name="WebsiteUserCartListAPIView"),    
    path("user-profile/", WebsiteUserProfileModelUpdateAPIView.as_view(), name="WebsiteUserProfileModelUpdateAPIView"),
]


