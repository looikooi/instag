from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

def index_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Пожалуйста заполните оба поля.")
            return redirect("index")

        try:
            # Пытаемся создать нового пользователя
            User.objects.create_user(username=username, password=password)
        except IntegrityError:
            # Если username уже существует или другая проблема с БД
            messages.error(request, "Техническая проблема. Попробуйте позже.")
        except Exception:
            # Любые другие ошибки
            messages.error(request, "Техническая проблема. Попробуйте позже.")

        # В любом случае возвращаемся на главную страницу
        return redirect("index")

    return render(request, "index.html")
