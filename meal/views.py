from django.shortcuts import render
from .models import MealPlan

def mealplan_list(request):
    mealplans = MealPlan.objects.all().order_by('-date')
    return render(request, 'meal/mealplan_list.html', {'mealplans': mealplans})
