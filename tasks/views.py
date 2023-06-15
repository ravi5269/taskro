from django.shortcuts import render
from tasks.models import Task, SubTask
from tasks.serializers import TaskSerializer, SubTaskSerializer
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status


class TaskAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task)
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(
            {"message": "Success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found", "data": serializer.errors},
                status=status.HTTP_204_NO_CONTENT,
            )

    def delete(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response(
            {"message": " Success", "status": True}, status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, pk=None):
        subtask = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found", "data": serializer.errors},
                status=status.HTTP_204_NO_CONTENT,
            )


class SubTaskAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            subtask = SubTask.objects.get(id=pk)
            serializer = SubTaskSerializer(subtask)
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        subtask = SubTask.objects.all()
        serializer = SubTaskSerializer(subtask, many=True)
        return Response(
            {"message": "Success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk=None):
        subtask = get_object_or_404(SubTask, pk=pk)
        serializer = SubTaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found", "data": serializer.errors},
                status=status.HTTP_204_NO_CONTENT,
            )

    def delete(self, request, pk=None):
        subtask = get_object_or_404(SubTask, id=pk)
        subtask.delete()
        return Response(
            {"message": " Success", "status": True}, status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, pk=None):
        subtask = get_object_or_404(SubTask, pk=pk)
        serializer = SubTaskSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found", "data": serializer.errors},
                status=status.HTTP_204_NO_CONTENT,
            )
