Add recipes in database

# Run in project directory
python3 manage.py shell

# Import the FoodRecipe model
from recipes.models import FoodRecipe

# Create instances of FoodRecipe and save them to the database

recipe1 = FoodRecipe.objects.create(title="Vegetable Stir Fry", recipe_type="VEG")

recipe2 = FoodRecipe.objects.create(title="Chicken Curry", recipe_type="NON-VEG")

recipe3 = FoodRecipe.objects.create(title="Pasta Primavera", recipe_type="VEG")

recipe4 = FoodRecipe.objects.create(title="Chicken momo", recipe_type="NON-VEG")

exit()

# Verify that the recipes have been added to the database
print(FoodRecipe.objects.all())

# migrate
python3 manage.py makemigrations

python3 manage.py migrate
