from textwrap import dedent, indent

from django.db import models

from pantry.models import Ingredient, Utensil


class Source(models.Model):
    """
    Where the recipe come from. It could be a book, a website, etc.
    """

    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return str(self.name)


class CuisineType(models.Model):
    """
    What the recipe is about: Veggie, French, Italian, etc.
    """

    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return str(self.name)


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

    def __str__(self) -> str:
        return str(self.name)

    
    def show(self):
        """
        Show what the recipe is about.
        """

        kinds = ', '.join(str(k) for k in self.kind.all())
        ingredients = '\n'.join(
            str(ingredient) for ingredient in self.ingredients.all()
        )
        utensils = '\n'.join(str(utentil) for utentil in self.utensils.all())

        tmpl = dedent(
            f"""
            {self.name}, a %(kinds)s recipe
            ---
            What you'll need to by:
            %(ingredients)s
            What you'll need in the kitchen:
            %(utensils)s
            """
        ) % {
            "kinds": kinds,
            "ingredients": indent(ingredients, "  - "),
            "utensils": indent(utensils, "  - "),
        }

        return tmpl
