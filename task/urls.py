from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_add, name='task_create'),
    path('task/<int:pk>/update/', views.task_edit, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('login_view/', views.login_view, name='login' ),
    path('register', register, name='register'),
]
