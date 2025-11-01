from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def index_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Пожалуйста заполните оба поля.")
            return redirect("index")

        # Проверяем, есть ли уже такой username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким именем уже существует.")
            return redirect("index")

        # Создаём нового пользователя
        User.objects.create_user(username=username, password=password)
        messages.success(request, f"Пользователь {username} создан!")
        return redirect("index")

    return render(request, "index.html")