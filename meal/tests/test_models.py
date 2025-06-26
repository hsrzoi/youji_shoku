import pytest
from meal.models import Ingredient, Meal, MealIngredient, MealPlan
from .factories import IngredientFactory, MealFactory, MealIngredientFactory, MealPlanFactory

@pytest.mark.django_db
def test_ingredient_str():
    ingredient = IngredientFactory(name="ブロッコリー")
    assert str(ingredient) == "ブロッコリー"

@pytest.mark.django_db
def test_meal_str():
    meal = MealFactory(name="ハンバーグ")
    assert str(meal) == "ハンバーグ"

@pytest.mark.django_db
def test_meal_ingredient_creation():
    mi = MealIngredientFactory()
    assert isinstance(mi.meal, Meal)
    assert isinstance(mi.ingredient, Ingredient)
    assert mi.quantity == "100g"

@pytest.mark.django_db
def test_mealplan_str():
    plan = MealPlanFactory()
    assert str(plan).endswith("の献立")
