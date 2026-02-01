# Скрипт для создания тестовых данных
# Запустить: python manage.py shell < load_sample_data.py

from products.models import Category, Product, Banner, ProductImage
from django.core.files.base import ContentFile
import os

print("Создание тестовых данных...")

# Создание категорий
categories_data = [
    {"name": "Бытовая химия", "slug": "bytovaya-himiya"},
    {"name": "Посуда", "slug": "posuda"},
    {"name": "Текстиль", "slug": "tekstil"},
    {"name": "Хозтовары", "slug": "hoztovary"},
]

categories = {}
for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        slug=cat_data["slug"],
        defaults={"name": cat_data["name"]}
    )
    categories[cat_data["slug"]] = category
    status = "создана" if created else "уже существует"
    print(f"Категория '{category.name}' {status}")

# Создание товаров
products_data = [
    {
        "title": "Порошок стиральный Premium",
        "slug": "poroshok-stiralnyj-premium",
        "description": "Высококачественный стиральный порошок для белого и цветного белья. Эффективно удаляет пятна при температуре от 30°C.",
        "price": 2500,
        "old_price": 3000,
        "category": "bytovaya-himiya",
        "promo": "sale",
    },
    {
        "title": "Набор кастрюль из нержавеющей стали",
        "slug": "nabor-kastryul-nerzhaveyushchaya-stal",
        "description": "Набор из 5 кастрюль различного объема. Подходит для всех типов плит, включая индукционные.",
        "price": 15000,
        "category": "posuda",
        "promo": "new",
    },
    {
        "title": "Комплект постельного белья",
        "slug": "komplekt-postelnogo-belya",
        "description": "100% хлопок, евро размер. Яркие цвета, не линяет при стирке.",
        "price": 8000,
        "old_price": 10000,
        "category": "tekstil",
        "promo": "sale",
    },
    {
        "title": "Моющее средство для посуды",
        "slug": "moyushchee-sredstvo-dlya-posudy",
        "description": "Концентрированное средство с ароматом лимона. Легко удаляет жир и загрязнения.",
        "price": 500,
        "category": "bytovaya-himiya",
        "promo": "none",
    },
    {
        "title": "Полотенце махровое",
        "slug": "polotentse-mahrovoe",
        "description": "Мягкое махровое полотенце 70x140 см. Отлично впитывает влагу.",
        "price": 1500,
        "category": "tekstil",
        "promo": "new",
    },
    {
        "title": "Швабра с отжимом",
        "slug": "shvabra-s-otzhimom",
        "description": "Удобная швабра с механизмом отжима. В комплекте 2 насадки из микрофибры.",
        "price": 3500,
        "category": "hoztovary",
        "promo": "none",
    },
    {
        "title": "Сковорода антипригарная 28 см",
        "slug": "skovoroda-antiprigarnaya-28sm",
        "description": "Сковорода с мраморным покрытием. Подходит для приготовления без масла.",
        "price": 4500,
        "old_price": 6000,
        "category": "posuda",
        "promo": "sale",
    },
    {
        "title": "Гель для стирки деликатных тканей",
        "slug": "gel-dlya-stirki-delikatnyh-tkanej",
        "description": "Бережно отстирывает шелк, шерсть и другие деликатные ткани.",
        "price": 1800,
        "category": "bytovaya-himiya",
        "promo": "new",
    },
]

products = []
for prod_data in products_data:
    category = categories.get(prod_data.pop("category"))
    product, created = Product.objects.get_or_create(
        slug=prod_data["slug"],
        defaults={**prod_data, "category": category}
    )
    products.append(product)
    status = "создан" if created else "уже существует"
    print(f"Товар '{product.title}' {status}")

# Создание баннеров (без изображений, их нужно загрузить через админку)
banners_data = [
    {
        "title": "Зимняя распродажа",
        "link": "",
        "order": 0,
    },
    {
        "title": "Новая коллекция посуды",
        "link": "",
        "order": 1,
    },
    {
        "title": "Скидки до 50%",
        "link": "",
        "order": 2,
    },
]

for banner_data in banners_data:
    banner, created = Banner.objects.get_or_create(
        title=banner_data["title"],
        defaults=banner_data
    )
    status = "создан" if created else "уже существует"
    print(f"Баннер '{banner.title}' {status}")

print("\n✅ Тестовые данные созданы успешно!")
print("\n⚠️  Примечание: Для баннеров и товаров нужно загрузить изображения через админ-панель.")
print("Админ-панель доступна по адресу: http://localhost:8000/admin/")
