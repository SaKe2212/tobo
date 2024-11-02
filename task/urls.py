from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_add, name='task_create'),
    path('task/<int:pk>/update/', views.task_edit, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
