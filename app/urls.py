from django.contrib import admin
from django.urls import path
from app import views

from django.contrib.auth import views as auth_views
from app.forms import LoginForm

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('delete-todo/<int:id>', views.deleteTodo, name="delete"),
    path('update-todo/<int:pk>', views.UpdateView.as_view(), name="update-todo"),
    path('about/', views.about, name="about"),
    path('contact/', views.ProfileView.as_view(), name="contact"),
    path('search/', views.search, name="search"),

    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('signup', views.CustomerRegistrationView.as_view(), name="signup"),
]
