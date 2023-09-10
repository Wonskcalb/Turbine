from django.db import models

from pantry.enums import IngredientType

from .managers import IngredientsManager


class Utensil(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    kind = models.CharField(max_length=64, choices=IngredientType.__members__.items())

    objects = IngredientsManager()

    def __str__(self):
        return self.name
