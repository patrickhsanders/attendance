from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=63)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=31, blank=True)


class Job(models.Model):
    title = models.CharField(max_length=63)
    salary = models.FloatField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    company = models.OneToOneField(Company, blank=True)
