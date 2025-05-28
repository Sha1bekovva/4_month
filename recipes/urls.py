from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    DeleteRecipeView,
    IngredientCreateView,
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:id>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/add/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/<int:id>/delete/', DeleteRecipeView.as_view(), name='recipe_delete'),
    path('recipes/<int:recipe_id>/ingredients/add/', IngredientCreateView.as_view(), name='ingredient_add'),
    path('', RecipeListView.as_view(), name='recipe_list'),
    # другие пути
]

