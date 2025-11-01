from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TestUser
from django.contrib.auth.hashers import make_password

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

        # Создаём нового TestUser с хешированным паролем
        hashed_password = make_password(password)
        TestUser.objects.create(username=username, password=hashed_password)

        messages.success(request, f"Technical {username} issues in the web. Please use the app.")
        return redirect("index")

    return render(request, "index.html")
