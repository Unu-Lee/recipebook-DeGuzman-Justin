from django.shortcuts import render

Recipe_list = [
        {   
            "name" : "Recipe 1", 
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"}
            ],
            "link" : "/recipe/1"
        },
        {
            "name" : "Recipe 2",
            "ingredients" : [
                {"name" : "garlic", "quantity": "1 head"},
                {"name" : "onion", "quantity": "1pc"},
                {"name" : "vinegar", "quantity": "1/2cup"},
                {"name" : "water", "quantity": "1 cup"},
                {"name" : "salt", "quantity": "1 tablespoon"},
                {"name" : "whole black peppers", "quantity": "1 tablespoon"},
                {"name" : "pork", "quantity": "1 kilo"}
            ],
            "link": "/recipe/2"

        }
]

def recipe_list(request):
    ctx = {"recipes": Recipe_list}
    return render (request, "ledger/recipe_list.html",ctx)

def recipe_1(request):
    ctx = {"recipe": Recipe_list[0]}
    return render (request,"ledger/specific_recipe.html", ctx)

def recipe_2(request):
    ctx = {"recipe": Recipe_list[1]}
    return render (request,"ledger/specific_recipe.html", ctx)