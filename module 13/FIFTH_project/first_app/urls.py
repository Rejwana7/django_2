from django.urls import path,include
from .import views

urlpatterns = [
  path('',views.home,name="homepage"),
  path('about/',views.about,name="aboutpage"),
  path('form/',views.submit_form,name="submit_form"),
  path('djangoform/',views.DjangoForm,name="django_form"),
  path('studentform/',views.Studentform,name="student_form"),
   path('checkpassword/',views.checkpassword,name="password"),
]

