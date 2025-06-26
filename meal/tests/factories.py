import factory
from meal.models import Ingredient, Meal, MealIngredient, MealPlan
from datetime import date

class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = "にんじん"
    category = "野菜"
    allergy_info = ""
    quantity = "1本"
    expiration_date = factory.LazyFunction(date.today)

class MealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meal

    name = "カレー"
    description = "おいしいカレー"

class MealIngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MealIngredient

    meal = factory.SubFactory(MealFactory)
    ingredient = factory.SubFactory(IngredientFactory)
    quantity = "100g"

class MealPlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MealPlan

    date = factory.LazyFunction(date.today)
    meal_type = "昼ごはん"
    menu = "カレーライス"
    description = "幼児向け"
