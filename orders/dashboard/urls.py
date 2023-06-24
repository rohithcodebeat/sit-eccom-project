from .views import DashboardOrderModelUpdateGenericAPIView
from django.urls import path 

urlpatterns = [
    path("update-order-api-view/<id>/", DashboardOrderModelUpdateGenericAPIView.as_view(), name="DashboardOrderModelUpdateGenericAPIView"),
]


