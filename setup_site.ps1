# Скрипт для финальной настройки сайта
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "   Финальная настройка сайта" -ForegroundColor Cyan
Write-Host "============================================`n" -ForegroundColor Cyan

$server = "89.207.255.6"

Write-Host "1️⃣  Проверка статуса контейнеров..." -ForegroundColor Yellow
ssh root@$server "cd /root/chistovie && docker-compose ps"

Write-Host "`n2️⃣  Проверка логов backend..." -ForegroundColor Yellow
ssh root@$server "cd /root/chistovie && docker-compose logs --tail=30 backend"

Write-Host "`n3️⃣  Выполнение миграций базы данных..." -ForegroundColor Yellow
ssh root@$server "cd /root/chistovie && docker-compose exec -T backend python manage.py migrate"

Write-Host "`n4️⃣  Сбор статических файлов..." -ForegroundColor Yellow
ssh root@$server "cd /root/chistovie && docker-compose exec -T backend python manage.py collectstatic --noinput"

Write-Host "`n5️⃣  Создание суперпользователя..." -ForegroundColor Yellow
Write-Host "Введите данные для админа:" -ForegroundColor Cyan
ssh root@$server "cd /root/chistovie && docker-compose exec backend python manage.py createsuperuser"

Write-Host "`n============================================" -ForegroundColor Green
Write-Host "   Сайт готов к работе!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host "`nFrontend: http://89.207.255.6:3000" -ForegroundColor White
Write-Host "API:      http://89.207.255.6:8000/api/" -ForegroundColor White
Write-Host "Admin:    http://89.207.255.6:8000/admin" -ForegroundColor White
Write-Host "`nДля входа в админ-панель используйте данные, которые вы только что создали.`n" -ForegroundColor Gray
