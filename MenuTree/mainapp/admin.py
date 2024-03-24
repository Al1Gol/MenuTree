from django.contrib import admin

from .models import Elements, Menus

# Добавляем имеющиеся таблицы в админку
admin.site.register(Menus)
admin.site.register(Elements)
