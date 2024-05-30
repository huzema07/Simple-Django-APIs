from django.shortcuts import render
from rest_framework import generics
from .models import Project , Task
from .serializers import ProjectSerializer , TaskSerializer

#Views for Project

class CreateProject(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class GetAllProjects(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer 

class GetProjectById(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer     
    lookup_field = "pk"     

class UpdateProject(generics.RetrieveUpdateDestroyAPIView):
     queryset = Project.objects.all()
     serializer_class = ProjectSerializer     
     lookup_field = "pk"     


class DeleteProject(generics.DestroyAPIView):
     queryset = Project.objects.all()
     serializer_class = ProjectSerializer     
     lookup_field = "pk"      







#***************************************************************************
# Views for Task

class CreateTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class GetAllTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 

class GetTaskById(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer     
    lookup_field = "pk"     


class UpdateTask(generics.RetrieveUpdateDestroyAPIView):
     queryset = Task.objects.all()
     serializer_class = TaskSerializer     
     lookup_field = "pk"     


class DeleteTask(generics.DestroyAPIView):
     queryset = Task.objects.all()
     serializer_class = TaskSerializer     
     lookup_field = "pk"      


