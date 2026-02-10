# Скрипт для обновления и перезапуска контейнеров на сервере
# Используйте этот скрипт вместо ручного ввода команд

$serverIp = "89.207.255.6"
$serverUser = "root"

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "   Обновление проекта на сервере" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Подключение к серверу $serverIp..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Вам нужно будет ввести пароль сервера несколько раз." -ForegroundColor Yellow
Write-Host ""

$commands = @"
cd /root/chistovie && \
echo '==== Получение обновлений из GitHub ====' && \
git pull && \
echo '==== Остановка контейнеров ====' && \
docker-compose down && \
echo '==== Пересборка backend ====' && \
docker-compose build backend && \
echo '==== Запуск всех контейнеров ====' && \
docker-compose up -d && \
sleep 5 && \
echo '==== Статус контейнеров ====' && \
docker-compose ps && \
echo '==== Логи backend (последние 30 строк) ====' && \
docker-compose logs --tail=30 backend
"@

ssh $serverUser@$serverIp $commands
