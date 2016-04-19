from django.core.management.base import BaseCommand, CommandError
from attendance.models import Register, DailyAttendance
from people.models import Student
from django.utils import timezone
from datetime import datetime

class Command(BaseCommand):
    help = "Creates daily register of all active students"

    def handle(self, *args, **options):
        active_students = Student.objects.filter(active=True)
        today = datetime.today()
        today_registers = Register.objects.filter(checkin__year=today.year, checkin__month=today.month, checkin__day=today.day)
        present_students = [register.student for register in today_registers]
        absent_students = [student for student in active_students if student not in present_students]

        daily_attendance = DailyAttendance(date=today)
        daily_attendance.save()

        daily_attendance.active_students=active_students
        daily_attendance.present=present_students
        daily_attendance.absent=absent_students
        daily_attendance.registers=today_registers
        daily_attendance.save()

        self.stdout.write(self.style.SUCCESS('Successfully created day\' attendance'))
