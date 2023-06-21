from django.urls import path, include 

urlpatterns = [
    path("dashboard/apis/", include("products.dashboard.urls")),
    path("app/apis/", include("products.app.urls")),
    path("app/website/", include("products.website.urls")),
]
