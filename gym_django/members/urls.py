from django.urls import path
from . import views
from gym_management_system.views import record_attendance
urlpatterns = [
    path('', views.login_user, name = 'login_user'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('record_attendance/', record_attendance, name='record_attendance'),
    path('register_user/', views.register_user, name='register_user'),
]