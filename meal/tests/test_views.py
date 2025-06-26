# meal/tests/test_views.py
import pytest
from django.urls import reverse
from meal.models import MealPlan, Ingredient
from .factories import MealPlanFactory, IngredientFactory

@pytest.mark.django_db
def test_mealplan_list_view_get(client):
    MealPlanFactory.create_batch(3)  # 3つ自動作成
    url = reverse("mealplan_list")
    response = client.get(url)
    assert response.status_code == 200
    assert b'<form' in response.content
    assert response.context['mealplans'].count() == 3


@pytest.mark.django_db
def test_mealplan_list_view_post(client):
    url = reverse("mealplan_list")
    data = {
        "date": "2025-06-25",
        "meal_type": "昼食",
        "menu": "ハンバーグとにんじん",
        "description": "手作り昼ごはん"
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert MealPlan.objects.filter(menu="ハンバーグとにんじん").exists()


@pytest.mark.django_db
def test_add_ingredient_post_valid(client):
    url = reverse("add_ingredient")
    data = {
        "name": "じゃがいも",
        "category": "野菜",
        "allergy_info": "",
        "quantity": "1個",
        "expiration_date": "2025-07-01"
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Ingredient.objects.filter(name="じゃがいも").exists()


@pytest.mark.django_db
def test_mealplan_detail_view(client):
    plan = MealPlanFactory(menu="魚とお味噌汁")
    url = reverse("mealplan_detail", kwargs={"pk": plan.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert "魚とお味噌汁" in response.content.decode("utf-8")
