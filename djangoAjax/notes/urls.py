from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Index,name="Home"),
    path('signup',views.Signup,name="signup"),
    path('login',views.LoginUser,name="Login"),
    path('logout',views.Logoutuser,name="Logout"),
    path('del',views.Logoutuser,name="crud_ajax_delete"),
    
]
