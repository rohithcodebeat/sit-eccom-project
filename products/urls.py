from django.urls import path, include 

urlpatterns = [
    path("dashboard/apis/", include("products.dashboard.urls")),
]
