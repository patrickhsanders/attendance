from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=31)
    rolling_admission = models.BooleanField(default=True)
    full_time = models.BooleanField(default=True)

    test_after_project = models.ForeignKey('projects.Project', related_name="display_test_after", null=True)

    def __str__(self):
        return self.name