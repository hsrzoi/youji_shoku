# meal/forms.py
from django import forms
from .models import Ingredient, MealPlan

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'category', 'expiration_date']

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['date', 'meal_type', 'menu']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}), 
        }