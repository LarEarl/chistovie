from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    ProductViewSet,
    CategoryViewSet,
    PromoViewSet,
    ProductByIdView,
    CategoryByIdView,
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'promos', PromoViewSet, basename='promo')

urlpatterns = [
    path('', include(router.urls)),
    path('products/id/<int:pk>/', ProductByIdView.as_view(), name='product-by-id'),
    path('categories/id/<int:pk>/', CategoryByIdView.as_view(), name='category-by-id'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
