from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_form_view, name='task-form'),
    path('delete/<int:task_id>/', views.delete_task, name='delete-task'),
    path('json/<int:task_id>/', views.task_json, name='task-json'),
]
