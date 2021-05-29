from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .forms import LoginForm




app_name = 'accounts'
urlpatterns = [
    path('signup',views.signup_view, name= 'signup'),
    path('login',views.login_view, name='login'),
    path('logout',views.logout_view, name= 'logout'),
    path('editprofile',views.edit_profile, name= 'editprofile'),
    
    path('<int:pk>/profile/',views.ProfilePageView.as_view(),name='profile'),
    
]