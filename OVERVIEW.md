# 📦 Chistovye - Краткий обзор проекта

## ✅ Что реализовано

### 🎨 Frontend (Nuxt 3)
- ✔️ Адаптивная верстка (Mobile, Tablet, Desktop)
- ✔️ Главная страница с баннерами
- ✔️ Карусель новинок и акций (Swiper.js)
- ✔️ Каталог товаров с фильтрацией по категориям
- ✔️ Детальная страница товара
- ✔️ Страница "О нас" с контактами
- ✔️ Современный UI с TailwindCSS
- ✔️ Плавные анимации и hover-эффекты
- ✔️ Lazy-loading изображений
- ✔️ SEO-оптимизация

### ⚙️ Backend (Django + DRF)
- ✔️ REST API для товаров, категорий, баннеров
- ✔️ JWT авторизация
- ✔️ Загрузка множественных изображений
- ✔️ Фильтрация, поиск, сортировка
- ✔️ Пагинация
- ✔️ CORS настройка
- ✔️ PostgreSQL база данных
- ✔️ Swagger/ReDoc документация

### 🎛️ Админ-панель (Django Admin)
- ✔️ CRUD для товаров с inline изображениями
- ✔️ CRUD для категорий
- ✔️ CRUD для баннеров
- ✔️ Предпросмотр изображений
- ✔️ Управление метками New/Sale
- ✔️ Удобный интерфейс

## 📂 Структура файлов

```
chistovye/
├── backend/
│   ├── config/
│   │   ├── settings.py         # Настройки Django
│   │   ├── urls.py             # Главные маршруты
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── products/
│   │   ├── models.py           # Product, Category, Banner, ProductImage
│   │   ├── serializers.py      # DRF сериализаторы
│   │   ├── views.py            # ViewSets
│   │   ├── admin.py            # Админ-панель
│   │   └── urls.py             # API маршруты
│   ├── manage.py
│   ├── requirements.txt        # Python зависимости
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/
│   ├── assets/
│   │   └── css/main.css        # Глобальные стили
│   ├── components/
│   │   ├── TheHeader.vue       # Шапка сайта
│   │   ├── TheFooter.vue       # Подвал сайта
│   │   ├── ProductCard.vue     # Карточка товара
│   │   ├── BannerCarousel.vue  # Карусель баннеров
│   │   └── ProductCarousel.vue # Карусель товаров
│   ├── composables/
│   │   └── useApi.js           # API методы
│   ├── layouts/
│   │   └── default.vue         # Основной layout
│   ├── pages/
│   │   ├── index.vue           # Главная страница
│   │   ├── about.vue           # О нас
│   │   └── products/
│   │       └── [slug].vue      # Детали товара
│   ├── stores/
│   │   └── products.js         # Pinia store
│   ├── app.vue
│   ├── nuxt.config.ts
│   ├── tailwind.config.js
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml          # Docker конфигурация
├── README.md                   # Полная документация
├── QUICKSTART.md              # Быстрый старт
├── API_DOCS.md                # API документация
└── DEPLOYMENT.md              # Деплой инструкции
```

## 🚀 Быстрый запуск

### Вариант 1: Локально

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### Вариант 2: Docker

```bash
docker-compose up -d
```

## 📊 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/products/` | Список товаров |
| GET | `/api/products/{slug}/` | Детали товара |
| GET | `/api/products/new_products/` | Новинки |
| GET | `/api/products/sale_products/` | Акции |
| GET | `/api/categories/` | Категории |
| GET | `/api/promos/` | Промоции |
| POST | `/api/token/` | JWT токен |

## 🎯 Основные возможности

### Для пользователей:
- Просмотр каталога товаров
- Фильтрация по категориям
- Поиск товаров
- Просмотр новинок и акций
- Детальная информация о товаре
- Адаптивный дизайн для всех устройств

### Для администраторов:
- Добавление/редактирование товаров
- Загрузка изображений
- Управление категориями
- Создание баннеров
- Установка меток New/Sale
- Управление ценами и скидками

## 🛠️ Технологии

**Frontend:**
- Nuxt 3
- Vue 3
- TailwindCSS
- GSAP
- Swiper.js
- Pinia

**Backend:**
- Django 5.0
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger/ReDoc

## 📱 Контакты

- **Телефон:** +7 701 263 50 25
- **Адрес:** Пичугина 162

## 📝 Следующие шаги

1. **Запустите проект** используя QUICKSTART.md
2. **Изучите API** в API_DOCS.md
3. **Добавьте тестовые данные** через админ-панель
4. **Настройте для production** по DEPLOYMENT.md

## 🔗 Полезные ссылки

- **Backend:** http://localhost:8000
- **Frontend:** http://localhost:3000
- **Админ:** http://localhost:8000/admin
- **API Docs:** http://localhost:8000/swagger

---

**Проект готов к использованию! 🎉**

Для получения подробной информации читайте:
- [README.md](./README.md) - Полная документация
- [QUICKSTART.md](./QUICKSTART.md) - Быстрый старт
- [API_DOCS.md](./API_DOCS.md) - API документация
- [DEPLOYMENT.md](./DEPLOYMENT.md) - Деплой
