# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт 10000
EXPOSE 10000

# Команда запуска:
# 1. Делаем миграции
# 2. Собираем статические файлы
# 3. Запускаем Gunicorn
CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn mysite.wsgi:application --bind 0.0.0.0:10000
