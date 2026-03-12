from .models import Recipe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeImageForm


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

    return render(request, "ledger/recipe_form.html", {"form": form})


@login_required
def add_image(request, pk):

    recipe = Recipe.objects.get(pk=pk)

    form = RecipeImageForm()

    if request.method == "POST":

        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():

            image = form.save(commit=False)
            image.recipe = recipe
            image.save()

            return redirect('specific_recipe', pk=pk)

    ctx = {"form": form, "recipe": recipe}

    return render(request, "ledger/add_image.html", ctx)
