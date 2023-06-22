from django.urls import path 
from .views import WebsiteUserWishListUpdateAPIView, WebsiteUserWishListRemoveAPIView, WebsiteUserWishListAPIView

urlpatterns = [
    path("add-to-wishlist/", WebsiteUserWishListUpdateAPIView.as_view(), name="WebsiteUserWishListUpdateAPIView"),
    path("remove-to-wishlist/", WebsiteUserWishListRemoveAPIView.as_view(), name="WebsiteUserWishListRemoveAPIView"),
    path("user-wishlist/", WebsiteUserWishListAPIView.as_view(), name="WebsiteUserWishListAPIView"),
    
]


