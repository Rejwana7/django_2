from django.urls import path 
#from firstapp.views import home
#from firstapp import views

from . import views

urlpatterns = [
    
    path('' , views.home),
]