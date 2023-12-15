from django.urls import path,include
from . import views


urlpatterns = [
   
 
    path('navigate/',views.navigate),
    path('context/',views.context),

]
