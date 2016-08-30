from rest_framework import serializers
from projects.serializers import ProjectSerializer
from .models import Student


class ActiveStudentSerializer(serializers.ModelSerializer):
    current_project = ProjectSerializer(many=False, read_only=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'current_project']
