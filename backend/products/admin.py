from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage, Category, Promo


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'is_primary', 'order', 'preview']
    readonly_fields = ['preview']
    
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px;" />',
                obj.image.url
            )
        return "Нет изображения"
    preview.short_description = 'Предпросмотр'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'price', 'promo', 
        'is_active', 'created_at'
    ]
    list_filter = ['category', 'promo', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Цены', {
            'fields': ('price', 'old_price')
        }),
        ('Промо и статус', {
            'fields': ('promo', 'is_active')
        }),
    )


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order', 'preview', 'created_at']
    list_filter = ['is_active']
    fields = ['title', 'image', 'link', 'is_active', 'order', 'preview']
    readonly_fields = ['preview']
    
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 150px; max-width: 300px;" />',
                obj.image.url
            )
        return "Нет изображения"
    preview.short_description = 'Предпросмотр'


admin.site.site_header = "Chistovye - Панель администратора"
admin.site.site_title = "Chistovye Admin"
admin.site.index_title = "Управление каталогом"
