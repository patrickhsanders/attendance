# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20160521_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='test_after_project',
        ),
    ]
