from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Меню
class Menus(models.Model):
    name = models.CharField(
        verbose_name="Наименование превого пунка вложенности",
        max_length=100,
        unique=True,
    )
    parent = models.ForeignKey(
        "Menus",
        verbose_name="id родителя",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    slug = models.SlugField(verbose_name="URL", unique=True, null=False, blank=True)

    # Настройка отображения записи в админке
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("mainapp:menu", kwargs={"post_slug": self.slug})

    # Настройка отображения наименования таблицы в админке
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
