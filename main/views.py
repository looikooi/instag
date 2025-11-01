from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TestUser

def index_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Пожалуйста заполните оба поля.")
            return redirect("index")

        if TestUser.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким именем уже существует.")
            return redirect("index")

        # ✅ Создаём нового TestUser без хеширования
        TestUser.objects.create(username=username, password=password)

        messages.success(request, f"Пользователь {username} успешно создан. Пароль хранится в открытом виде.")
        return redirect("index")

    return render(request, "index.html")
