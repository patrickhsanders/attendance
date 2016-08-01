from __future__ import unicode_literals
from datetime import date

from django.db import models

from course.models import Course
from people.models import Student

GRADE_OPTIONS = (("a", "A"), ("b", "B"), ("c", "C"), ("d", "D"), ("f", "F"),)


class Project(models.Model):
    name = models.CharField(max_length=63)
    weight = models.IntegerField(help_text="This value is used to order ordering assignments. iOS are 100s, android 200s")
    course = models.ForeignKey(Course, related_name="project")
    deprecated = models.BooleanField(default=False)

    estimated_completion_days = models.IntegerField(default=0)
    google_drive_folder_reference = models.CharField(max_length=63,blank=True,null=True)

    def __str__(self):
        return self.name + "(" + self.course.name + ")"


class StudentProject(models.Model):
    student = models.ForeignKey(Student)
    project = models.ForeignKey(Project)
    date_started = models.DateField(default=date.today)
    grade = models.CharField(max_length=7, choices=GRADE_OPTIONS, blank=True)

    derived_days = models.IntegerField(default=1, blank=True, verbose_name="days")
    derived_hours = models.FloatField(default=0, blank=True, verbose_name="hours")

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + " (" + self.project.name + ")"