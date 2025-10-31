from django.contrib import admin
from .models import TestUser

@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # показываем username и пароль в списке
