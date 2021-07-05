# apps/home/admin.py

# Django locals
from django.contrib import admin

# Django local
from apps.product.models import Category

# Register your models here.
admin.site.register(Category)