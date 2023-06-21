from django.urls import path
from .views import DasboardProductCategoryModelListCreateAPIView, DasboardProductBrandModelListCreateAPIView, DasboardProductColorModelListCreateAPIView, DasboardProductDescriptionModelListCreateAPIView, DasboardProductImageModelListCreateAPIView, DasboardProductServiceModelListCreateAPIView, DasboardProductVariationModelListCreateAPIView, DashboardProductModelCreateAPIView, DasboardProductModelListAPIView, DasboardProductCategoryModelGenericAPIView, DasboardProductBrandModelGenericAPIView, DasboardProductColorModelGenericAPIView, DasboardProductDescriptionModelGenericAPIView ,DasboardProductImageModelGenericAPIView, DasboardProductServiceModelGenericAPIView, DasboardProductVariationModelGenericAPIView

urlpatterns = [
    path("product-category-list-create-api-view/", DasboardProductCategoryModelListCreateAPIView.as_view(), name="DasboardProductCategoryModelListCreateAPIView"),
    path("product-category-list-create-api-view/<id>/", DasboardProductCategoryModelGenericAPIView.as_view(), name="DasboardProductCategoryModelGenericAPIView"),
    
    path("product-brand-list-create-api-view/", DasboardProductBrandModelListCreateAPIView.as_view(), name="DasboardProductBrandModelListCreateAPIView"),
    path("product-brand-list-create-api-view/<id>/", DasboardProductBrandModelGenericAPIView.as_view(), name="DasboardProductBrandModelGenericAPIView"),
    
    path("product-color-list-create-api-view/", DasboardProductColorModelListCreateAPIView.as_view(), name="DasboardProductColorModelListCreateAPIView"),
    path("product-color-list-create-api-view/<id>/", DasboardProductColorModelGenericAPIView.as_view(), name="DasboardProductColorModelGenericAPIView"),
    
    path("product-descripiton-list-create-api-view/", DasboardProductDescriptionModelListCreateAPIView.as_view(), name="DasboardProductDescriptionModelListCreateAPIView"),
    path("product-descripiton-list-create-api-view/<id>/", DasboardProductDescriptionModelGenericAPIView.as_view(), name="DasboardProductDescriptionModelGenericAPIView"),
    
    path("product-image-list-create-api-view/", DasboardProductImageModelListCreateAPIView.as_view(), name="DasboardProductImageModelListCreateAPIView"),
    path("product-image-list-create-api-view/<id>/", DasboardProductImageModelGenericAPIView.as_view(), name="DasboardProductImageModelGenericAPIView"),
    
    path("product-service-list-create-api-view/", DasboardProductServiceModelListCreateAPIView.as_view(), name="DasboardProductServiceModelListCreateAPIView"),
    path("product-service-list-create-api-view/<id>/", DasboardProductServiceModelGenericAPIView.as_view(), name="DasboardProductServiceModelListCreateAPIView"),

    path("product-variation-list-create-api-view/", DasboardProductVariationModelListCreateAPIView.as_view(), name="DasboardProductVariationModelListCreateAPIView"),    
    path("product-variation-list-create-api-view/<id>/", DasboardProductVariationModelGenericAPIView.as_view(), name="DasboardProductVariationModelGenericAPIView"),    
    
    path("product-create-api-view/", DashboardProductModelCreateAPIView.as_view(), name="DashboardProductModelCreateAPIView"),
    path("product-list-api-view/", DasboardProductModelListAPIView.as_view(), name="DasboardProductModelListAPIView"),
]
