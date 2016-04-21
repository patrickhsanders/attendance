from django.db import models
from people.models import Student
from projects.models import Project
from django.utils import timezone

# Create your models here.

class Register(models.Model):
    student = models.ForeignKey(Student)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(blank=True, null=True)
    forgot_to_checkout = models.BooleanField(default=False)

    current_curriculum_project = models.ForeignKey(Project, blank=True, null=True)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + "(" + str(self.checkin.month) + "/" + str(self.checkin.day) + "/" + str(self.checkin.year) + " " + str(self.checkin.hour) + ":" + str(self.checkin.minute) + ")"

class DailyAttendance(models.Model):
    date = models.DateField()
    active_students = models.ManyToManyField(Student, blank=True, related_name="active_students+")
    present = models.ManyToManyField(Student, blank=True, related_name="present+")
    absent = models.ManyToManyField(Student, blank=True, related_name="absent+")

    registers = models.ManyToManyField(Register, blank=True)

    def __str__(self):
        return "Attendance for " + str(self.date.month) + "/" + str(self.date.day) + "/" + str(self.date.year)