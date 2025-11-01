from django.contrib import admin
from .models import TestUser

@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # показываем username и пароль в списке
    fields = ('username', 'password')        # поля, которые редактируем при просмотре
    search_fields = ('username',)            # поиск по имени пользователя
