# Generated by Django 5.0.3 on 2024-03-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_alter_menus_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menus",
            name="slug",
            field=models.SlugField(blank=True, unique=True, verbose_name="URL"),
        ),
    ]
