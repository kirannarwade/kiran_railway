from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('update/<int:pk>', views.update_todo, name='update'),
    path('delete/<int:pk>', views.delete_todo, name='delete')
]
