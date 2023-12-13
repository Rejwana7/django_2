from django.urls import path
#from .views import contact
from . import views

urlpatterns = [
  
    path("courses/",views.courses),
    #ekhane er url gulo project er url er sathe connect korte hobe
    path("about/",views.about),
    path("",views.home),
  
]
