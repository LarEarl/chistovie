# DEPLOYMENT GUIDE

## Деплой на VPS/VDS сервер

### Требования
- Ubuntu 20.04+ / Debian 11+
- Docker & Docker Compose
- Nginx
- SSL сертификат (Let's Encrypt)

### 1. Подготовка сервера

```bash
# Обновление системы
sudo apt update && sudo apt upgrade -y

# Установка Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Установка Docker Compose
sudo apt install docker-compose -y

# Установка Nginx
sudo apt install nginx -y

# Установка Certbot для SSL
sudo apt install certbot python3-certbot-nginx -y
```

### 2. Клонирование проекта

```bash
cd /var/www
sudo git clone <your-repo-url> chistovye
cd chistovye
```

### 3. Настройка переменных окружения

```bash
# Backend
cd backend
sudo nano .env
```

Пример `.env`:
```env
SECRET_KEY=your-very-secret-and-long-random-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_NAME=chistovye_db
DB_USER=postgres
DB_PASSWORD=strong_password_here
DB_HOST=db
DB_PORT=5432
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

```bash
# Frontend
cd ../frontend
sudo nano .env
```

```env
NUXT_PUBLIC_API_BASE=https://yourdomain.com/api
```

### 4. Запуск через Docker Compose

```bash
cd /var/www/chistovye

# Сборка и запуск контейнеров
sudo docker-compose up -d --build

# Проверка статуса
sudo docker-compose ps

# Создание суперпользователя Django
sudo docker-compose exec backend python manage.py createsuperuser
```

### 5. Настройка Nginx

```bash
sudo nano /etc/nginx/sites-available/chistovye
```

```nginx
# Backend
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /media/ {
        alias /var/www/chistovye/backend/media/;
    }

    location /static/ {
        alias /var/www/chistovye/backend/staticfiles/;
    }

    client_max_body_size 20M;
}

# Frontend
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# Активация конфигурации
sudo ln -s /etc/nginx/sites-available/chistovye /etc/nginx/sites-enabled/

# Проверка конфигурации
sudo nginx -t

# Перезапуск Nginx
sudo systemctl restart nginx
```

### 6. Настройка SSL (Let's Encrypt)

```bash
# Получение сертификата
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com -d api.yourdomain.com

# Автоматическое обновление
sudo certbot renew --dry-run
```

### 7. Настройка брандмауэра

```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

## Деплой на специализированных платформах

### Heroku

**Backend:**
```bash
cd backend
heroku create chistovye-api
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

**Frontend:**
```bash
cd frontend
heroku create chistovye-web
heroku config:set NUXT_PUBLIC_API_BASE=https://chistovye-api.herokuapp.com/api
git push heroku main
```

### Vercel (Frontend)

```bash
cd frontend
npm install -g vercel
vercel
# Следуйте инструкциям
```

### DigitalOcean App Platform

1. Создайте новое приложение
2. Подключите GitHub репозиторий
3. Настройте компоненты:
   - Backend: Python/Django
   - Frontend: Node.js/Nuxt
   - Database: PostgreSQL
4. Добавьте переменные окружения
5. Деплой!

### Railway

1. Зарегистрируйтесь на railway.app
2. New Project → Deploy from GitHub
3. Добавьте PostgreSQL
4. Настройте переменные окружения
5. Автоматический деплой при push

## Полезные команды для production

```bash
# Просмотр логов
sudo docker-compose logs -f backend
sudo docker-compose logs -f frontend

# Перезапуск сервисов
sudo docker-compose restart backend
sudo docker-compose restart frontend

# Обновление кода
cd /var/www/chistovye
sudo git pull
sudo docker-compose up -d --build

# Бэкап базы данных
sudo docker-compose exec db pg_dump -U postgres chistovye_db > backup.sql

# Восстановление базы данных
sudo docker-compose exec -T db psql -U postgres chistovye_db < backup.sql

# Очистка Docker
sudo docker system prune -a
```

## Мониторинг

### Установка Prometheus + Grafana (опционально)

```bash
# Добавить в docker-compose.yml сервисы мониторинга
# Настроить метрики Django
# Создать дашборды в Grafana
```

## Безопасность

1. **Firewall:** Открыты только 80, 443, 22 порты
2. **SSH:** Только ключи, отключить пароли
3. **Django:** DEBUG=False, SECRET_KEY уникальный
4. **PostgreSQL:** Сильный пароль, не exposed наружу
5. **Backup:** Автоматические бэкапы БД и media
6. **Updates:** Регулярно обновлять зависимости
7. **HTTPS:** Обязательно использовать SSL

## Производительность

1. **Кэширование:** Redis для Django cache
2. **CDN:** CloudFlare для статики
3. **Compression:** Gzip в Nginx
4. **Database:** Индексы, query optimization
5. **Images:** Оптимизация размеров, WebP формат

---

После деплоя проект доступен на вашем домене! 🚀
