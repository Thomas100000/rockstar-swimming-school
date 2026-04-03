from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rockstar-portal-99/', admin.site.urls),
    path('', include('core.urls')),
]
