from __future__ import unicode_literals
from django.db import models
from datetime import date
import datetime

# Create your models here.
class OperatingSystem(models.Model):
    friendly_name = models.CharField(max_length=31, help_text="e.g. Lion, El Capitan, etc")
    granular_name = models.CharField(max_length=31, help_text="e.g. 10.11.2", unique=True)

    def __str__(self):
        return self.friendly_name + " (" + self.granular_name + ")"

class Xcode(models.Model):
    version_number = models.CharField(max_length=31, help_text="e.g. 7.2.1", unique=True)

    def __str__(self):
        return self.version_number

class ComputerModel(models.Model):
    COMPUTER_MODELS = [('imac',"iMac"),('macbook pro',"Macbook Pro"), ('macbook_air','Macbook Air')]
    YEAR_CHOICES = []
    #for year in range(datetime.datetime.now().year - 10,(datetime.datetime.now().year):
    for year in range(datetime.datetime.now().year - 10,datetime.datetime.now().year):
        YEAR_CHOICES.append((year,year))
    computer_model = models.CharField(max_length=31,choices=COMPUTER_MODELS)
    year = models.IntegerField(choices=YEAR_CHOICES)

    def __str__(self):
        return [item for item in self.COMPUTER_MODELS if item[0] == self.computer_model][0][1] + " (" + str(self.year) + ")"

class Computer(models.Model):
    name = models.CharField("Asset identifier",
                            max_length=31,
                            unique=True,)
    computer_model = models.ForeignKey(ComputerModel, null=True, blank=True)
    # operating_system = models.ForeignKey(OperatingSystem, null=True, blank=True)
    # xcode_version = models.ForeignKey(Xcode, null=True, blank=True)

    def __str__(self):
        return self.name
