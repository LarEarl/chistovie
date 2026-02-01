from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Категория товаров"""
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL slug')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    PROMO_CHOICES = [
        ('none', 'Нет'),
        ('new', 'Новинка'),
        ('sale', 'Акция'),
    ]
    
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(max_length=300, unique=True, verbose_name='URL slug')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        verbose_name='Цена'
    )
    old_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0)],
        verbose_name='Старая цена'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='products',
        verbose_name='Категория'
    )
    promo = models.CharField(
        max_length=10, 
        choices=PROMO_CHOICES, 
        default='none',
        verbose_name='Промо метка'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    @property
    def is_sale(self):
        return self.promo == 'sale'


class ProductImage(models.Model):
    """Изображения товара"""
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='images',
        verbose_name='Товар'
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Изображение')
    is_primary = models.BooleanField(default=False, verbose_name='Главное изображение')
    order = models.IntegerField(default=0, verbose_name='Порядок')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.product.title} - изображение {self.id}"


class Promo(models.Model):
    """Промоция для главной страницы"""
    title = models.CharField(max_length=200, blank=True, verbose_name='Заголовок')
    image = models.ImageField(upload_to='hero/', verbose_name='Изображение')
    link = models.URLField(blank=True, verbose_name='Ссылка')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    order = models.IntegerField(default=0, verbose_name='Порядок')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Промоция'
        verbose_name_plural = 'Промоции'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title or f"Промоция {self.id}"
