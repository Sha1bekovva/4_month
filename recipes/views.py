from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.all().order_by('-id')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'recipes/ingredient_form.html'

    def form_valid(self, form):
        recipe_pk = self.kwargs.get('pk')
        form.instance.recipe = get_object_or_404(Recipe, pk=recipe_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.kwargs.get('pk')})
