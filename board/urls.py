from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main.as_view()),
    path('main/create/', views.main_create.as_view(), name="main_create_url"),
    path('day/', views.day.as_view()),
    path('day/create/', views.day_create.as_view(), name="day_create_url"),
    path('sub/', views.sub.as_view()),
    path('sub/create/', views.sub_create.as_view(), name="sub_create_url"),
]