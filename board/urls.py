from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main.as_view()),
    path('main/create/', views.main_create.as_view(), name="main_create_url"),
    #path('day/', views.day.as_view()),
    #path('sub/', views.sub.as_view()),
]