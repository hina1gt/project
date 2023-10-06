from django.shortcuts import render
from .permissions import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from task.models import *
from rest_framework.response import Response
from rest_framework.status import *

@api_view(['GET', 'POST'])
@permission_classes([CustomUserPermission])
def customuser(request):
    if request.method == 'GET':
        customusers = CustomUser.objects.all()
        serializer = CustomUserSerializer(customusers, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CustomUserDetailPermission])
def customuser_detail(request, pk):
    customuser = CustomUser.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = CustomUserSerializer(customuser, context={'request': request})
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(customuser, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customuser.adelete()
        return Response(status=HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
@permission_classes([TaskPermission])
def task(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = CustomUserSerializer(tasks, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.date)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TaskDetailPermission])
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(customuser)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TaskSerializer(customuser, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([ProjectPermission])
def project(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.date)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([ProjectDetailPermission])
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(customuser, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=HTTP_204_NO_CONTENT)

