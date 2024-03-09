from django.urls import path, include, re_path
from . import api

urlpatterns = [
    path('tasks/', api.TaskListApi.as_view()),
    path('task/<int:pk>/', api.TaskApi.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

