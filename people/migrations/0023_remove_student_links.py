# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 03:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0022_remove_student_work_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='links',
        ),
    ]
