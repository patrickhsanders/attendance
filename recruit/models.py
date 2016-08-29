from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=63)
    company = models.CharField(max_length=63)
    salary = models.FloatField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    city = models.CharField(max_length=31, blank=True)
