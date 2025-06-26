from django.urls import path
from . import views

urlpatterns = [
    path('', views.mealplan_list, name='mealplan_list'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('add_mealplan/', views.add_mealplan, name='add_mealplan'),
    path('meal/<int:pk>/edit/', views.mealplan_edit, name='mealplan_edit'),
    path('meal/<int:pk>/delete/', views.mealplan_delete, name='mealplan_delete'),
    path('meal/<int:pk>/', views.mealplan_detail, name='mealplan_detail'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/<int:pk>/edit/', views.ingredient_edit, name='ingredient_edit'),
    path('ingredients/<int:pk>/delete/', views.ingredient_delete, name='ingredient_delete'),

]
