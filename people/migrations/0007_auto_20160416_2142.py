# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20160416_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='computer',
        ),
        migrations.AddField(
            model_name='student',
            name='uses_own_laptop',
            field=models.BooleanField(default=True),
        ),
    ]
