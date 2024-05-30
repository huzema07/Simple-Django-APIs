from rest_framework import serializers
from .models import Project , Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name","id", "description" ]



class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    class Meta:
        model = Task
        fields = ["title", "description" ,"due_date", "completed", "project" ]