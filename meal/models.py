from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    allergy_info = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='MealIngredient')

    def __str__(self):
        return self.name

class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True)  # 例: "100g"など
