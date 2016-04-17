from __future__ import unicode_literals

from django.db import models

from course.models import Course

# Create your models here.
class Project(models.Model):
    COURSE_OPTIONS = (('ios','iOS Full-time'),('android','Android Full-time'),('swift','iOS Part-time (Swift)'))
    name = models.CharField(max_length=63)
    weight = models.IntegerField(help_text="This value is used to order ordering assignments. iOS are 100s, android 200s")
    course = models.ForeignKey(Course)
    # description = models.TextField(null=True, blank=True)
    # project_file = models.FileField(upload_to='uploads/projects', null=True, blank=True)
    # public_link_to_project = models.URLField(null=True,blank=True)
    # nextProject = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name + "(" + self.course.name + ")"
