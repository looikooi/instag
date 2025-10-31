# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Собираем статические файлы Django
RUN python manage.py collectstatic --noinput

# Открываем порт 10000 (Render автоматически перенаправляет)
EXPOSE 10000

# Команда запуска
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:10000"]
