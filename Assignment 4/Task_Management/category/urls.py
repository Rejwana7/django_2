from django.urls import path,include
from .import views

urlpatterns = [
    
    path('add/', views.Add_Category, name="add_category"),
    path('edit/<int:id>', views.Edit_Category, name="edit_category"),
  
  

]