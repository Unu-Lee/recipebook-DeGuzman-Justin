from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):

    class META:
        model = Recipe
        fields = '__all__'