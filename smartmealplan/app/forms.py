from django import forms
from .models import Recipe

class IngredientSearchForm(forms.Form):
    ingredients = forms.CharField(label='Enter Ingredients', widget=forms.TextInput(attrs={'class': 'form-control'}))