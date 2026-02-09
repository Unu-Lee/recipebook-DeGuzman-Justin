from django.urls import path
from .views import recipe_list, recipe_1, recipe_2 # Import your view functions

urlpatterns = [
    # localhost:8000/recipes/list
    path('recipes/list', recipe_list, name='recipe_list'),]