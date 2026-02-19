from django.urls import path
from .views import recipe_list, specific_recipe

urlpatterns = [
    path('',recipe_list, name='home'),
    path('<int:pk>', specific_recipe, name = 'specific_recipe')
]