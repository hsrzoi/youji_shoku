from django.contrib import admin
from .models import Ingredient, MealPlan

admin.site.register(Ingredient)
admin.site.register(MealPlan)