# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_deprecated'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='estimated_completion_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='google_drive_folder_reference',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]
