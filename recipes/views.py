from rest_framework import generics
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer

class FoodRecipeList(generics.ListAPIView):
    serializer_class = FoodRecipeSerializer

    def get_queryset(self):
        queryset = FoodRecipe.objects.all()
        recipe_type = self.request.query_params.get('recipe_type', None)
        if recipe_type is not None:
            queryset = queryset.filter(recipe_type=recipe_type)
        return queryset
