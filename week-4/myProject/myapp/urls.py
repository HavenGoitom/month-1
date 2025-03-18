from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('toggle_complete/<int:todo_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete_task/<int:todo_id>/', views.delete_task, name='delete_task'),
]
