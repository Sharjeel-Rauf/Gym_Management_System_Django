from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_view, name="home"),
    path("delete/<int:member_id>/", views.delete_member_view, name="delete_member"),
    path("new/", views.create_member_view, name="create_member"),
    path("update/<int:member_id>/", views.update_member_view, name="update_member"),
    path("search_member", views.search_member, name="search_member"),
    path('record_attendance/', views.record_attendance, name='record_attendance'),
    path('membership/<int:member_id>/', views.member_detail, name='member_detail'),
    path('monthly_attendance/<int:member_id>/', views.monthly_attendance, name='monthly_attendance'),
]