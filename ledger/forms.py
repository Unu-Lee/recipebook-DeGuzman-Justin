from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):

    class META:
        model = Recipe
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):

    class META:
        model = RecipeImage
        fields = ["image", "description"]