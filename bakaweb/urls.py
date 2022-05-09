import imp
from django.contrib import admin
from django.urls import path, include
import bakaweb_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bakaweb_app.urls')),
]
