from django.contrib import admin

from .models import Menus


# Добавляем имеющиеся таблицы в админку
@admin.register(Menus)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
