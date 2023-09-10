from typing import TYPE_CHECKING

from django.db.models import Manager, QuerySet

from pantry.enums import IngredientType

if TYPE_CHECKING:
    from pantry.models import Ingredient


class IngredientsManager(Manager):
    model: "Ingredient"

    def in_category(self, *categories: IngredientType) -> QuerySet["Ingredient"]:
        return self.filter(kind__in=categories)
