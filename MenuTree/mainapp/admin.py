from django.contrib import admin

from .models import Menus


# Добавляем имеющиеся таблицы в админку
@admin.register(Menus)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "slug")
    list_display_links = ("slug",)
    list_editable = ["name"]
    list_filter = ("parent",)
    prepopulated_fields = {"slug": ("name",)}
