from django.urls import path 
from .views import AppProductModelListAPIView

urlpatterns = [
    path("product-list-api-view/", AppProductModelListAPIView.as_view(), name="AppProductModelListAPIView"),
]


