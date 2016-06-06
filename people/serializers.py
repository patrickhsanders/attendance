from .models import Student
from projects.models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name',)


class ActiveStudentSerializer(serializers.ModelSerializer):
    current_project = ProjectSerializer(many=False, read_only=True)

    class Meta:
        model = Student
        fields = ['first_name','last_name','email','current_project']

