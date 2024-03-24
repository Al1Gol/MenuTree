from django.contrib import admin

from .models import Menus

# Добавляем имеющиеся таблицы в админку
admin.site.register(Menus)
