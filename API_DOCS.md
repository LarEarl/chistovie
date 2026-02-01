# API Documentation

## Base URL
```
http://localhost:8000/api
```

## Database

По умолчанию API ожидает PostgreSQL. Параметры берутся из переменных окружения:
- `DB_NAME` (default: `chistovye`)
- `DB_USER` (default: `postgres`)
- `DB_PASSWORD` (default: `postgres`)
- `DB_HOST` (default: `localhost`)
- `DB_PORT` (default: `5432`)

Для локального запуска создайте базу и пользователя либо переопределите переменные в `.env`.

## Authentication

API использует JWT (JSON Web Tokens) для аутентификации.

### Получение токена
```http
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Использование токена
Добавьте заголовок Authorization в запросы:
```
Authorization: Bearer {access_token}
```

### Обновление токена
```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "your_refresh_token"
}
```

## Products API

### Список товаров
```http
GET /api/products/
```

**Query параметры:**
- `page` - номер страницы (default: 1)
- `page_size` - количество на странице (default: 12)
- `category` - ID категории для фильтрации
- `promo` - фильтр по промо (new, sale, none)
- `search` - поиск по названию и описанию
- `ordering` - сортировка (price, -price, created_at, -created_at)

**Response:**
```json
{
  "count": 20,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Название товара",
      "slug": "nazvanie-tovara",
      "price": "1000.00",
      "old_price": "1500.00",
      "category": 1,
      "category_name": "Категория",
      "promo": "sale",
      "is_sale": true,
      "images": [
        "http://localhost:8000/media/products/2025/12/05/image.jpg"
      ],
      "created_at": "2025-12-05T12:00:00Z"
    }
  ]
}
```

### Детали товара
```http
GET /api/products/{slug}/
```

**Response:**
```json
{
  "id": 1,
  "title": "Название товара",
  "slug": "nazvanie-tovara",
  "description": "Подробное описание товара",
  "price": "1000.00",
  "old_price": "1500.00",
  "category": 1,
  "category_name": "Категория",
  "promo": "sale",
  "is_sale": true,
  "is_active": true,
  "images": [
    {
      "id": 1,
      "image": "http://localhost:8000/media/products/2025/12/05/image.jpg",
      "is_primary": true,
      "order": 0
    }
  ],
  "created_at": "2025-12-05T12:00:00Z",
  "updated_at": "2025-12-05T14:30:00Z"
}
```

### Детали товара по ID
```http
GET /api/products/id/{id}/
```

### Новинки
```http
GET /api/products/new_products/
```

Возвращает до 8 товаров с меткой "new".

### Акции
```http
GET /api/products/sale_products/
```

Возвращает до 8 товаров с меткой "sale".

### Создание товара
```http
POST /api/products/
Authorization: Bearer {token}
Content-Type: multipart/form-data

{
  "title": "Новый товар",
  "slug": "novyy-tovar",
  "description": "Описание",
  "price": "1000.00",
  "old_price": "1200.00",
  "category": 1,
  "promo": "new",
  "is_active": true,
  "uploaded_images": [file1, file2]
}
```

### Обновление товара
```http
PUT /api/products/{slug}/
Authorization: Bearer {token}
Content-Type: multipart/form-data

{
  "title": "Обновленное название",
  "price": "900.00"
}
```

### Удаление товара
```http
DELETE /api/products/{slug}/
Authorization: Bearer {token}
```

### Удаление изображения
```http
DELETE /api/products/{slug}/images/{image_id}/
Authorization: Bearer {token}
```

## Categories API

### Список категорий
```http
GET /api/categories/
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Электроника",
    "slug": "elektronika",
    "created_at": "2025-12-05T10:00:00Z"
  }
]
```

### Детали категории
```http
GET /api/categories/{slug}/
```

### Детали категории по ID
```http
GET /api/categories/id/{id}/
```

### Создание категории
```http
POST /api/categories/
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "Новая категория",
  "slug": "novaya-kategoriya"
}
```

### Обновление категории
```http
PUT /api/categories/{slug}/
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "Обновленное название"
}
```

### Удаление категории
```http
DELETE /api/categories/{slug}/
Authorization: Bearer {token}
```

## Banners API

### Список баннеров
```http
GET /api/promos/
```

Неавторизованные пользователи видят только активные баннеры.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Зимняя распродажа",
    "image": "http://localhost:8000/media/banners/banner1.jpg",
    "link": "https://example.com",
    "is_active": true,
    "order": 0,
    "created_at": "2025-12-05T10:00:00Z"
  }
]
```

### Детали баннера
```http
GET /api/promos/{id}/
```

### Создание баннера
```http
POST /api/promos/
Authorization: Bearer {token}
Content-Type: multipart/form-data

{
  "title": "Новый баннер",
  "image": file,
  "link": "https://example.com",
  "is_active": true,
  "order": 0
}
```

### Обновление баннера
```http
PUT /api/promos/{id}/
Authorization: Bearer {token}
Content-Type: multipart/form-data

{
  "title": "Обновленный баннер",
  "is_active": false
}
```

### Удаление баннера
```http
DELETE /api/promos/{id}/
Authorization: Bearer {token}
```

## Error Responses

### 400 Bad Request
```json
{
  "field_name": ["Error message"]
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error."
}
```

## Rate Limiting

API использует стандартные лимиты Django. По умолчанию ограничений нет.

## CORS

CORS настроен для работы с:
- http://localhost:3000
- http://127.0.0.1:3000

Для production добавьте свой домен в `CORS_ALLOWED_ORIGINS` в settings.py.

## Примеры использования

### JavaScript (fetch)
```javascript
// Получить товары
const response = await fetch('http://localhost:8000/api/products/')
const data = await response.json()

// Создать товар с токеном
const formData = new FormData()
formData.append('title', 'Новый товар')
formData.append('price', '1000')
formData.append('slug', 'novyy-tovar')

const response = await fetch('http://localhost:8000/api/products/', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_TOKEN'
  },
  body: formData
})
```

### Python (requests)
```python
import requests

# Получить товары
response = requests.get('http://localhost:8000/api/products/')
products = response.json()

# Создать товар с токеном
headers = {'Authorization': 'Bearer YOUR_TOKEN'}
data = {
    'title': 'Новый товар',
    'slug': 'novyy-tovar',
    'price': '1000',
}
response = requests.post(
    'http://localhost:8000/api/products/',
    headers=headers,
    data=data
)
```

---

Полная интерактивная документация доступна на:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/
