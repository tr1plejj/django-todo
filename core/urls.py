from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('add_task/', views.add_task, name='add_task'),
    path('task_edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('complete_task/<int:pk>/', views.complete_task, name='complete_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task')
]
