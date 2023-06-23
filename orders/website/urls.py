from django.urls import path 
from .views import WebsiteOrderModelCreateAPIView

urlpatterns = [
    path("user-order/", WebsiteOrderModelCreateAPIView.as_view(), name="WebsiteOrderModelCreateAPIView"),
]