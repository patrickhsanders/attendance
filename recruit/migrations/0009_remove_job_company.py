# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0008_auto_20160907_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
    ]
