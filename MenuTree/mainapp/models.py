from django.db import models

# Список меню
class Menus(models.Model):
    name = models.CharField(verbose_name="Наименование меню", max_length=100)

    def __str__(self):
        return self.name
    

# Первый уровень вложенности
class Nesting_1(models.Model):
    name = models.CharField(verbose_name="Наименование превого пунка вложенности", max_length=100)

    def __str__(self):
        return self.name

# Второй уровень вложенности
class Nesting_2(models.Model):
    name = models.CharField(verbose_name="Наименование второго пунка вложенности", max_length=100)

    def __str__(self):
        return self.name

# Третий уровень вложенности
class Nesting_3(models.Model):
    name = models.CharField(verbose_name="Наименование 3 пунка вложенности", max_length=100)

    def __str__(self):
        return self.name