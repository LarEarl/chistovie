# Dockerfile для Frontend (Nuxt)

FROM node:18-alpine AS build

WORKDIR /app

# Копирование package files
COPY package*.json ./

# Установка зависимостей
RUN npm ci

# Копирование исходников
COPY . .

# Сборка приложения
RUN npm run build

# Production образ
FROM node:18-alpine

WORKDIR /app

# Копирование собранного приложения
COPY --from=build /app/.output /app/.output
COPY --from=build /app/package*.json ./

# Установка только production зависимостей
RUN npm ci --only=production

# Порт
EXPOSE 3000

# Переменные окружения
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

# Запуск
CMD ["node", ".output/server/index.mjs"]
