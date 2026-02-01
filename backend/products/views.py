from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Product, Category, Promo, ProductImage
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySerializer,
    PromoSerializer,
)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение на чтение для всех, на запись только для администраторов"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet для товаров"""
    queryset = Product.objects.filter(is_active=True).prefetch_related('images', 'category')
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'promo', 'is_active']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer
    
    @action(detail=False, methods=['get'])
    def new_products(self, request):
        """Получить новинки"""
        products = self.queryset.filter(promo='new')[:8]
        serializer = ProductListSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def sale_products(self, request):
        """Получить товары со скидкой"""
        products = self.queryset.filter(promo='sale')[:8]
        serializer = ProductListSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['delete'], url_path='images/(?P<image_id>[^/.]+)')
    def delete_image(self, request, slug=None, image_id=None):
        """Удалить изображение товара"""
        product = self.get_object()
        try:
            image = ProductImage.objects.get(id=image_id, product=product)
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProductImage.DoesNotExist:
            return Response(
                {'detail': 'Изображение не найдено'}, 
                status=status.HTTP_404_NOT_FOUND
            )


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'


class PromoViewSet(viewsets.ModelViewSet):
    """ViewSet для промоций"""
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list' and not self.request.user.is_staff:
            queryset = queryset.filter(is_active=True)
        return queryset


class ProductByIdView(generics.RetrieveAPIView):
    """Получить товар по id (альтернатива slug)"""
    queryset = Product.objects.filter(is_active=True).prefetch_related('images', 'category')
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]


class CategoryByIdView(generics.RetrieveAPIView):
    """Получить категорию по id (альтернатива slug)"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
