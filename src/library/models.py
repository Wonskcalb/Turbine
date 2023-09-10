from django.db import models

from pantry.models import Ingredient, Utensil


class Source(models.Model):
    """
    Where the recipe come from. It could be a book, a website, etc.
    """

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class CuisineType(models.Model):
    """
    What the recipe is about: Veggie, French, Italian, etc.
    """

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    A recipe, containing ingredients, steps, etc
    """

    name = models.CharField(max_length=256)
    origin = models.ForeignKey(
        to=Source, null=True, default=None, blank=True, on_delete=models.SET_NULL
    )
    kind = models.ManyToManyField(to=CuisineType)

    utensils = models.ManyToManyField(to=Utensil)
    ingredients = models.ManyToManyField(to=Ingredient)

    def __str__(self):
        return self.name
