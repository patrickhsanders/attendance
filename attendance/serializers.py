from rest_framework import serializers
from attendance.models import DailyAttendance
from people.serializers import ActiveStudentSerializer

class PresentStudentSerializer(serializers.ModelSerializer):
    present = ActiveStudentSerializer(many=True, read_only=True)
    absent = ActiveStudentSerializer(many=True, read_only=True)

    class Meta:
        model = DailyAttendance
        fields = ['date','present','absent']
