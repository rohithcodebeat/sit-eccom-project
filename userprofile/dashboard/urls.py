from django.urls import path 
from .views import DasboardUserCartListAPIView, DashboardUserWishListAPIView


urlpatterns = [
    path("users-cart/", DasboardUserCartListAPIView.as_view(), name="DasboardUserCartListAPIView"),
    path("users-wishlist/", DashboardUserWishListAPIView.as_view(), name="DashboardUserWishListAPIView"),

]

