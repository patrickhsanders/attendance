from __future__ import unicode_literals
from datetime import date

from django.db import models

from course.models import Course
from people.models import Student


class Project(models.Model):
    name = models.CharField(max_length=63)
    weight = models.IntegerField(help_text="This value is used to order ordering assignments. iOS - 100s, android 200s")
    course = models.ForeignKey(Course, related_name="project")
    deprecated = models.BooleanField(default=False)

    estimated_completion_days = models.IntegerField(default=0)
    google_drive_folder_reference = models.CharField(max_length=63, blank=True, null=True)

    google_drive_link = models.CharField(max_length=127, blank=True, null=True)

    def __str__(self):
        return self.name + "(" + self.course.name + ")"


class StudentProject(models.Model):
    student = models.ForeignKey(Student)
    project = models.ForeignKey(Project)
    date_started = models.DateField(default=date.today)

    derived_days = models.IntegerField(default=1, blank=True, verbose_name="days")
    derived_hours = models.FloatField(default=0, blank=True, verbose_name="hours")

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + " (" + self.project.name + ")"
