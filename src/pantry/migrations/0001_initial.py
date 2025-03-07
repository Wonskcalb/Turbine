# Generated by Django 4.2.5 on 2023-09-10 17:55

from django.db import migrations, models

import pantry.enums


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("FISH", pantry.enums.IngredientType["FISH"]),
                            ("MEAT", pantry.enums.IngredientType["MEAT"]),
                            ("VEGETABLE", pantry.enums.IngredientType["VEGETABLE"]),
                            ("STARCHY", pantry.enums.IngredientType["STARCHY"]),
                            ("HERBS", pantry.enums.IngredientType["HERBS"]),
                            ("SPICES", pantry.enums.IngredientType["SPICES"]),
                            ("DAIRY", pantry.enums.IngredientType["DAIRY"]),
                        ],
                        max_length=64,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Utensil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
        ),
    ]
