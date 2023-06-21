from django.urls import path
from .views import DasboardProductCategoryModelListCreateAPIView, DasboardProductBrandModelListCreateAPIView, DasboardProductColorModelListCreateAPIView, DasboardProductDescriptionModelListCreateAPIView, DasboardProductImageModelListCreateAPIView, DasboardProductServiceModelListCreateAPIView, DasboardProductVariationModelListCreateAPIView, DashboardProductModelCreateAPIView, DasboardProductModelListAPIView

urlpatterns = [
    path("product-category-list-create-api-view/", DasboardProductCategoryModelListCreateAPIView.as_view(), name="DasboardProductCategoryModelListCreateAPIView"),
    path("product-brand-list-create-api-view/", DasboardProductBrandModelListCreateAPIView.as_view(), name="DasboardProductBrandModelListCreateAPIView"),
    path("product-color-list-create-api-view/", DasboardProductColorModelListCreateAPIView.as_view(), name="DasboardProductColorModelListCreateAPIView"),
    path("product-descripiton-list-create-api-view/", DasboardProductDescriptionModelListCreateAPIView.as_view(), name="DasboardProductDescriptionModelListCreateAPIView"),
    path("product-image-list-create-api-view/", DasboardProductImageModelListCreateAPIView.as_view(), name="DasboardProductImageModelListCreateAPIView"),
    path("product-service-list-create-api-view/", DasboardProductServiceModelListCreateAPIView.as_view(), name="DasboardProductServiceModelListCreateAPIView"),
    path("product-variation-list-create-api-view/", DasboardProductVariationModelListCreateAPIView.as_view(), name="DasboardProductVariationModelListCreateAPIView"),    
    path("product-create-api-view/", DashboardProductModelCreateAPIView.as_view(), name="DashboardProductModelCreateAPIView"),
    path("product-list-api-view/", DasboardProductModelListAPIView.as_view(), name="DasboardProductModelListAPIView"),
]
