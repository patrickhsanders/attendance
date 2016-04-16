from __future__ import unicode_literals

from django.db import models
from people.models import Student
from assets.models import Computer
# Create your models here.

class Place(models.Model):
    FROND_CHOICES = (('west','West - Near Kitchen'),
                    ('middle','Middle'),
                    ('east','East'),
                    ('windows','Window adjacent'),)
    frond = models.CharField(max_length=31, choices = FROND_CHOICES)
    seat = models.IntegerField(help_text="Northmost seat is 1, increasing clockwise from there")
    student = models.ForeignKey(Student, null=True, blank=True, limit_choices_to={'active':True},)
    computer = models.ForeignKey(Computer, null=True, blank=True)

    def __str__(self):
        return str([item for item in self.FROND_CHOICES if item[0] == self.frond][0][1]) + " " + str(self.seat)
