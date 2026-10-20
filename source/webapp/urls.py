from django.urls import path
from webapp.views import task_list_view, task_create_view, task_delete_view

urlpatterns = [
    path('', task_list_view),
    path('tasks/add/', task_create_view),
    path('tasks/<int:task_id>/delete/', task_delete_view),
]
