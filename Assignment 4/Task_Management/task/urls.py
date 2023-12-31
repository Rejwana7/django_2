from django.urls import path,include
from .import views

urlpatterns = [
    
    path('add/', views.Add_Task,name="add_task"),
    path('edit/<int:id>', views.Edit_Task,name="edit_task"),
    path('deletet/<int:id>', views.Delete_Task,name="delete_task"),
  
  

]