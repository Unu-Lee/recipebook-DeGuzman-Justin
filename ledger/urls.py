from django.urls import path
from .views import recipe_list, specific_recipe, recipe_add, add_image

urlpatterns = [
    path("recipe/list", recipe_list, name="recipe_list"),
    path("recipe/<int:pk>", specific_recipe, name="specific_recipe"),
    path('recipe/add', recipe_add, name='recipe_add'),
    path('recipe/<int:pk>/add_image', add_image, name='add_image')
]
