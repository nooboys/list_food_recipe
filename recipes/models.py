from django.db import models

class FoodRecipe(models.Model):
    VEG = 'VEG'
    NON_VEG = 'NON-VEG'
    RECIPE_TYPE_CHOICES = [
        (VEG, 'Vegetarian'),
        (NON_VEG, 'Non-Vegetarian'),
    ]
    class Meta:
        app_label = 'recipes'
    
    title = models.CharField(max_length=100)
    recipe_type = models.CharField(max_length=8, choices=RECIPE_TYPE_CHOICES)

    def __str__(self):
        return self.title
