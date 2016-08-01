from .models import Student
from projects.serializers import ProjectSerializer
from rest_framework import serializers

class ActiveStudentSerializer(serializers.ModelSerializer):
    current_project = ProjectSerializer(many=False, read_only=True)

    class Meta:
        model = Student
        fields = ['first_name','last_name','email','current_project']
