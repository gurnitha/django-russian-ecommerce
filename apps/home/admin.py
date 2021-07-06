# apps/home/models.py

# Django modules
from django.contrib import admin

# Django locals
from apps.home.models import Setting


class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']


# Register your models here.
admin.site.register(Setting, SettingtAdmin)
