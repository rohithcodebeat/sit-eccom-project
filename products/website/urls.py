from django.urls import path 
from .views import WebsiteProductModelListAPIView

urlpatterns = [
    path("product-list-api-view/", WebsiteProductModelListAPIView.as_view(), name="WebsiteProductModelListAPIView"),
]

