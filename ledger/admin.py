from django.contrib import admin
from .models import Profile, Ingredient, Recipe, RecipeIngredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile)
admin.site.register(Ingredient)
