from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/',views.signUp,name='signup'),
    path('login/',views.user_login,name='loginpage'),
    path('Passchange/',views.pass_change,name='passchange'),
    path('Passchange2/',views.pass_change2,name='passchange2'),
    path('logout/',views.user_logout,name='logoutpage'),
    path('profile/',views.profile,name='profilepage'),
 ]