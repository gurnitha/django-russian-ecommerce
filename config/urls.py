# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

# Django locals
from apps.home import urls 

urlpatterns = [
    path('', include('apps.home.urls')),
    path('admin/', admin.site.urls),
]
