# config/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Django locals
from apps.home import urls 

urlpatterns = [
    path('', include('apps.home.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)