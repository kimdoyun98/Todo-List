from django.urls import path
from . import views


urlpatterns = [
    path('', views.Todo_main.as_view(), name='todo_main'),
]