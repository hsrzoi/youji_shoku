from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import IngredientForm, MealPlanForm
from .models import MealPlan,Ingredient
from django.utils import timezone

def mealplan_list(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = MealPlanForm()

    mealplans = MealPlan.objects.all().order_by('-date')
    return render(request, 'meal/mealplan_list.html', {
        'form': form,
        'mealplans': mealplans
    })

def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')  
    else:
        form = IngredientForm()
    return render(request, 'meal/add_ingredient.html', {'form': form})

def add_mealplan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mealplan_list')  # 既にある一覧ページ
    else:
        form = MealPlanForm()
    return render(request, 'meal/add_mealplan.html', {'form': form})

def mealplan_detail(request, pk):
    mealplan = get_object_or_404(MealPlan, pk=pk)
    return render(request, 'meal/mealplan_detail.html', {'mealplan': mealplan})


def mealplan_edit(request, pk):
    mealplan = get_object_or_404(MealPlan, pk=pk)
    if request.method == 'POST':
        form = MealPlanForm(request.POST, instance=mealplan)
        if form.is_valid():
            form.save()
            return redirect('mealplan_list')
    else:
        form = MealPlanForm(instance=mealplan)

    return render(request, 'meal/mealplan_edit.html', {'form': form, 'mealplan': mealplan})

def mealplan_delete(request, pk):
    mealplan = get_object_or_404(MealPlan, pk=pk)
    if request.method == 'POST':
        mealplan.delete()
        return redirect('mealplan_list')
    return render(request, 'meal/mealplan_delete_confirm.html', {'mealplan': mealplan})

def ingredient_list(request):
    today = timezone.now().date()
    ingredients = Ingredient.objects.all().order_by('expiration_date')
    return render(request, 'meal/ingredient_list.html', {
        'ingredients': ingredients,
        'today': today,
    })

def ingredient_edit(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient_edit.html', {'form': form})

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'ingredient_confirm_delete.html', {'ingredient': ingredient})
