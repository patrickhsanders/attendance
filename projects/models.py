from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    COURSE_OPTIONS = (('ios','iOS Full-time'),('android','Android Full-time'),('swift','iOS Part-time (Swift)'))
    name = models.CharField(max_length=31)
    course = models.CharField(max_length=31, choices = COURSE_OPTIONS)

    description = models.TextField(null=True, blank=True)

    project_file = models.FileField(upload_to='uploads/projects', null=True, blank=True)
    public_link_to_project = models.URLField(null=True,blank=True)

    nextProject = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name
