"""
URL configuration for task management endpoints.

This module defines API routes for creating, retrieving,
updating, and deleting tasks.
"""
from django.urls import path
from .views import create_task, get_tasks, update_task_status, delete_task

urlpatterns = [
    path("tasks/", create_task),                       # Create a new task
    path("tasks/all/", get_tasks),                     # Retrieve all tasks
    path("tasks/<str:task_id>/", update_task_status),  # Update the status of a specific task by ID
    path("tasks/<str:task_id>/delete/", delete_task),  # Delete a specific task by ID
]
