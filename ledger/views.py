from .models import Recipe
from django.shortcuts import render



def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html",ctx)

def specific_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe": recipe}
    return render(request,"ledger/specific_recipe.html", ctx)

