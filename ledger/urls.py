from django.urls import path
from .views import recipe_list, specific_recipe

urlpatterns = [
    path("recipe/list", recipe_list, name="recipe_list"),
    path("recipe/<int:pk>", specific_recipe, name="specific_recipe"),
]
