from django.urls import path
from . import views

urlpatterns = [
    path('', views.mealplan_list, name='mealplan_list'),
]
