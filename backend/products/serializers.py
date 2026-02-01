from rest_framework import serializers
from .models import Product, ProductImage, Category, Promo


class ProductImageSerializer(serializers.ModelSerializer):
    """Сериализатор изображений товара"""
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_primary', 'order']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at']


class ProductListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка товаров"""
    images = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'slug', 'price', 'old_price', 
            'category', 'category_name', 'promo', 'is_sale',
            'images', 'created_at'
        ]
    
    def get_images(self, obj):
        images = obj.images.all()
        if images:
            request = self.context.get('request')
            return [request.build_absolute_uri(img.image.url) for img in images]
        return []


class ProductDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детального просмотра товара"""
    images = ProductImageSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'slug', 'description', 'price', 
            'old_price', 'category', 'category_name', 'promo', 
            'is_sale', 'is_active', 'images', 'uploaded_images',
            'created_at', 'updated_at'
        ]
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = Product.objects.create(**validated_data)
        
        for idx, image in enumerate(uploaded_images):
            ProductImage.objects.create(
                product=product,
                image=image,
                is_primary=(idx == 0),
                order=idx
            )
        
        return product
    
    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if uploaded_images:
            for idx, image in enumerate(uploaded_images):
                max_order = instance.images.count()
                ProductImage.objects.create(
                    product=instance,
                    image=image,
                    order=max_order + idx
                )
        
        return instance


class PromoSerializer(serializers.ModelSerializer):
    """Сериализатор промоций"""
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Promo
        fields = ['id', 'title', 'image', 'link', 'is_active', 'order', 'created_at']
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
