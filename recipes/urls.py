from django.urls import path
from .views import FoodRecipeList

urlpatterns = [
    path('recipes/', FoodRecipeList.as_view(), name='recipe-list'),
]
