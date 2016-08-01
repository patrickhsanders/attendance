from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=31)
    rolling_admission = models.BooleanField(default=True)
    full_time = models.BooleanField(default=True)

    course_fee = models.FloatField(blank=True)

    test_after_project = models.ForeignKey('projects.Project', related_name="display_test_after", blank=True, null=True)

    def __str__(self):
        return self.name