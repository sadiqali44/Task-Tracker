"""
API views for task management.

This module provides REST API endpoints to create, retrieve,
update, and delete tasks stored in MongoDB.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from datetime import datetime
from .db import get_task_collection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Allowed task states
TASK_STATUS = ["TODO", "IN_PROGRESS", "DONE"]

@csrf_exempt
@api_view(["POST"])
def create_task(request):
    """
    Create a new task.

    Expects:
        JSON body with:
            - title (str): Title of the task

    Returns:
        200 OK: Task ID if created successfully
        400 Bad Request: If title is missing
    """
    task_collection = get_task_collection()

    title = request.data.get("title")
    if not title:
        return Response({"error": "Title is required"}, status=400)

    task = {
        "title": title,
        "status": "TODO",
        "createdAt": datetime.utcnow()
    }

    result = task_collection.insert_one(task)
    return Response({"id": str(result.inserted_id)}, status=200)

@csrf_exempt
@api_view(["GET"])
def get_tasks(request):
    """
    Retrieve all tasks.

    Returns:
        200 OK: List of task objects
    """
    task_collection = get_task_collection()
    tasks = []

    for task in task_collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)

    return Response(tasks, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["PATCH"])
def update_task_status(request, task_id):
    """
    Update the status of an existing task.

    Rules:
        - Allowed statuses: TODO, IN_PROGRESS, DONE
        - Direct transition from TODO → DONE is not allowed

    Args:
        task_id (str): MongoDB ObjectId of the task

    Expects:
        JSON body with:
            - status (str)

    Returns:
        200 OK: If status updated
        400 Bad Request: If task/status is invalid
    """
    task_collection = get_task_collection()
    new_status = request.data.get("status")

    if new_status not in TASK_STATUS:
        return Response(
            {"error": "Invalid status"},
            status=status.HTTP_400_BAD_REQUEST
        )

    task = task_collection.find_one({"_id": ObjectId(task_id)})

    if not task:
        return Response(
            {"error": "Task not found"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Rule: TODO → DONE not allowed
    if task["status"] == "TODO" and new_status == "DONE":
        return Response(
            {"error": "Cannot move directly from TODO to DONE"},
            status=status.HTTP_400_BAD_REQUEST
        )

    task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"status": new_status}}
    )

    return Response(
        {"message": "Status updated"},
        status=status.HTTP_200_OK
    )

@csrf_exempt
@api_view(["DELETE"])
def delete_task(request, task_id):
    """
    Delete a task by ID.

    Args:
        task_id (str): MongoDB ObjectId of the task

    Returns:
        200 OK: If task deleted
        400 Bad Request: If task not found
    """
    task_collection = get_task_collection()
    task = task_collection.find_one({"_id": ObjectId(task_id)})

    if not task:
        return Response(
            {"error": "Task not found"},
            status=status.HTTP_400_BAD_REQUEST
        )

    task_collection.delete_one({"_id": ObjectId(task_id)})

    return Response(
        {"message": "Task deleted successfully"},
        status=status.HTTP_200_OK
    )
