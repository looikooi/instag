# Используем официальный Python образ
FROM python:3.12-slim

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Открываем порт для Render
EXPOSE 10000

# Команда запуска: миграции → collectstatic → gunicorn
CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn mysite.wsgi:application --bind 0.0.0.0:10000
