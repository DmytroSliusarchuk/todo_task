from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @swagger_auto_schema(
        operation_description="Create a new task",
        request_body=TaskSerializer,
        responses={
            201: TaskSerializer,
            400: openapi.Response(description="Bad request"),
        },
    )
    def create(self, request, *args, **kwargs):
        """
        Create a new task.
        """

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Get a task by id",
        responses={
            200: TaskSerializer,
            404: openapi.Response(description="Task not found"),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Get a task by id.
        """

        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Get list of tasks", responses={200: TaskSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        """
        Get list of tasks.
        """

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a task by id",
        responses={
            204: openapi.Response(description="Task deleted"),
            404: openapi.Response(description="Task not found"),
        },
    )
    def destroy(self, request, *args, **kwargs):
        """
        Delete a task by id.
        """

        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=TaskSerializer,
        operation_description="Update a task by id",
        responses={
            200: TaskSerializer,
            400: openapi.Response(description="Bad request"),
            404: openapi.Response(description="Task not found"),
        },
    )
    def update(self, request, *args, **kwargs):
        """
        Update a task by id.
        """

        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=no_body,
        operation_description="Mark a task as completed",
        responses={
            200: TaskSerializer,
            400: openapi.Response(description="Task is already completed"),
            404: openapi.Response(description="Task not found"),
        },
    )
    def partial_update(self, request, pk=None):
        """
        Mark a task as completed.
        """

        task = self.get_object()
        if task.is_completed:
            return Response({"status": "task is already completed."}, status=status.HTTP_400_BAD_REQUEST)

        task.is_completed = True
        task.save()
        return Response({"status": "task marked as completed."}, status=status.HTTP_200_OK)
