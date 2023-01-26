"""Crudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Kiran Admin"
admin.site.site_title = "Kiran Admin Portal"
admin.site.index_title = "Welcome to Kiran Admin Portal"


handler404 = 'app.views.error_404'
handler403 = 'app.views.error_403'
handler400 = 'app.views.error_400'


urlpatterns = [
    path('admin-kmn/', admin.site.urls),
    path('', include('app.urls'))
]
