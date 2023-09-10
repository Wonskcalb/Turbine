from django.contrib import admin

from library.models import CuisineType, Recipe, Source


@admin.register(Source)
class AdminSource(admin.ModelAdmin):
    list_display = ["name"]

    # TODO add:
    # - quick link to recipes from each
    # - stats,
    # - source


@admin.register(CuisineType)
class AdminCuisineType(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ["name", "origin"]
