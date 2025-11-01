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

# Собираем статические файлы Django
RUN python manage.py collectstatic --no-input

# Делаем миграции (только если база доступна на этапе сборки; чаще делают на Pre-Deploy)
# RUN python manage.py migrate

# Открываем порт 10000 (Render автоматически перенаправляет)
EXPOSE 10000

# Команда запуска
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:10000"]
