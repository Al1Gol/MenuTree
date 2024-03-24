# Generated by Django 5.0.3 on 2024-03-24 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_alter_elements_name_alter_elements_parent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="elements",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mainapp.elements",
                verbose_name="id родителя",
            ),
        ),
    ]
