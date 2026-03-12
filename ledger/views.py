from .models import Recipe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html", ctx)


@login_required
def specific_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe": recipe}
    return render(request, "ledger/specific_recipe.html", ctx)

@login_required
def recipe_add(request):
    
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save()
            return redirect('specific_recipe', pk=recipe.pk)
    
    return render(request,"ledger/specific_form.html", {"form": form})
    

