from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    is_allergen = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    age_min_months = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title
