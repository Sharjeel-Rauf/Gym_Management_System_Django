
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gym_management_system.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('members.urls')),
]
