from django.urls import path,include
from.import views

urlpatterns = [
  
    path('',views.DjangoForm,name="djangoform"),
    path("model/",views.model_form ,name="modelform"),
     path("delete/<int:roll>", views.delete_student ,name="deletestudent")
]