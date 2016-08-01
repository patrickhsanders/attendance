from .models import Course
from rest_framework import serializers
from projects.serializers import ProjectSerializer

class CourseSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('name', 'project')

