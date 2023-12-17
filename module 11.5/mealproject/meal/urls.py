from django.urls import path
from . import views

urlpatterns = [
   
    path('meal-details/', views.food_details , name='meal-details'),
]
