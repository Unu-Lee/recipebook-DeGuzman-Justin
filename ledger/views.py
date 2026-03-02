from .models import Recipe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html", ctx)


@login_required(login_url="accounts/login")
def specific_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe": recipe}
    return render(request, "ledger/specific_recipe.html", ctx)
