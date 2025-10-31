# Базовый образ Python
FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY . .

# Собираем статические файлы Django
RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 10000

# Запуск сервера
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:10000"]
