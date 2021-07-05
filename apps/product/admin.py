# apps/home/admin.py

# Django locals
from django.contrib import admin

# Django local
from apps.product.models import Category, Product, Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status']
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)