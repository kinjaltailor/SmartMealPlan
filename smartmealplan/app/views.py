from django.shortcuts import render
from .models import Recipe
from .forms import IngredientSearchForm

# Create your views here.


def index(request):
    form = IngredientSearchForm()
    recipes = None
    if request.method == 'POST':
        form = IngredientSearchForm(request.POST)
        if form.is_valid():
            user_ingredients = form.cleaned_data['ingredients'].lower().split(', ')
            recipes = Recipe.objects.filter(ingredients__icontains=user_ingredients[0])
    return render(request, 'index.html', {'form': form, 'recipes': recipes})