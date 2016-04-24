from __future__ import unicode_literals

from django.db import models

from datetime import date

from course.models import Course
from people.models import Student

GRADE_OPTIONS = (("a", "A"), ("b", "B"), ("c", "C"), ("d", "D"), ("f", "F"),)

# Create your models here.
class Project(models.Model):
    # COURSE_OPTIONS = (('ios','iOS Full-time'),('android','Android Full-time'),('swift','iOS Part-time (Swift)'))
    name = models.CharField(max_length=63)
    weight = models.IntegerField(help_text="This value is used to order ordering assignments. iOS are 100s, android 200s")
    course = models.ForeignKey(Course)

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

#
# class Test(models.Model):
#
#     name = models.CharField(max_length=63)
#     weight = models.IntegerField(help_text="This value is used to order ordering assignments. iOS are 100s, android 200s")
#
#     def __str__(self):
#         return self.name
#
# class StudentTest(models.Model):
#     student = models.ForeignKey(Student)
#     test = models.ForeignKey(Test)
#     date_handed_out = models.DateField(default=date.today)
#     date_turned_in = models.DateTimeField(blank=True)
#
#     grade = models.CharField(max_length=7, choices=GRADE_OPTIONS, blank=True)
#
#     def __str__(self):
#         return self.student.first_name + " " + self.student.last_name + " (" + self.test.name + ")"