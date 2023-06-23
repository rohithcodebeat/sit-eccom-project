from django.urls import path 
from .views import WebsiteOrderModelCreateAPIView, WebsiteOrderModelFromCartCreateAPIView

urlpatterns = [
    path("user-order/", WebsiteOrderModelCreateAPIView.as_view(), name="WebsiteOrderModelCreateAPIView"),
    path("user-order-from-cart/", WebsiteOrderModelFromCartCreateAPIView.as_view(), name="WebsiteOrderModelFromCartCreateAPIView"),
]