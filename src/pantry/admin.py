from django.contrib import admin

from .models import Ingredient, Utensil


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Utensil)
class AdminUtensil(admin.ModelAdmin):
    list_display = ["name"]
