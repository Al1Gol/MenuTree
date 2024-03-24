from django.db import models


# Список меню
class Menus(models.Model):
    name = models.CharField(verbose_name="Наименование меню", max_length=100)

    # Настройка отображения записи в админке
    def __str__(self):
        return self.name

    # Настройка отображения наименования таблицы в админке
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


# Элементы меню
class Elements(models.Model):
    menu_id = models.ForeignKey(
        "Menus", verbose_name="id меню", on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name="Наименование превого пунка вложенности", max_length=100
    )
    parent = models.ForeignKey(
        "Elements", verbose_name="id родителя", on_delete=models.CASCADE, blank=True
    )

    # Настройка отображения записи в админке
    def __str__(self):
        return self.name

    # Настройка отображения наименования таблицы в админке
    class Meta:
        verbose_name = "Элементы меню"
        verbose_name_plural = "Элементы меню"
