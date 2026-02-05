"""
Root URL configuration for the Django project.

This module routes requests to the admin interface
and includes API endpoints from the tasks application.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")), # Task management API routes
]
