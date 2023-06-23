from django.urls import path 
from .views import WebsiteProductReviewModelCreateAPIView

urlpatterns = [
    path("product-review-create-api/", WebsiteProductReviewModelCreateAPIView.as_view(), name="WebsiteProductReviewModelCreateAPIView")
]
