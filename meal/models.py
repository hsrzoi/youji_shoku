from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    allergy_info = models.CharField(max_length=100, blank=True)
    quantity = models.CharField(max_length=50, blank=True, null=True)  # 量など
    expiration_date = models.DateField(null=True, blank=True)

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

class MealPlan(models.Model):
    date = models.DateField()
    meal_type = models.CharField(max_length=100)  # ← これが必要
    menu = models.TextField()
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return f"{self.date}の献立"