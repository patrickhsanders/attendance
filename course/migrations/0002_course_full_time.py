# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='full_time',
            field=models.BooleanField(default=True),
        ),
    ]
