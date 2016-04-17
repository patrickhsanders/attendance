from django.db import models
from people.models import Student
from projects.models import Project

# Create your models here.

class Register(models.Model):
    student = models.ForeignKey(Student)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(blank=True, null=True)
    forgot_to_checkout = models.BooleanField(default=False)

    current_project = models.CharField(max_length=63, blank=True)
    current_curriculum_project = models.ForeignKey(Project, blank=True, null=True)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + "(" + str(self.checkin.month) + "/" + str(self.checkin.day) + "/" + str(self.checkin.year) + " " + str(self.checkin.hour) + ":" + str(self.checkin.minute) + ")"