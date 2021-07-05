# apps/home/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.home import views

urlpatterns = [
    path('', views.homepage, name='home')
]
