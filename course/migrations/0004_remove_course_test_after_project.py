# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_test_after_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='test_after_project',
        ),
    ]
