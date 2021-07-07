# apps/home/models.py

# Django modules
from django.contrib import admin

# Django locals
from apps.home.models import Setting, ContactMessage


class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']


# Register your models here.
admin.site.register(Setting, SettingtAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
