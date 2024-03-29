# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 02:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160222_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='computer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_using', to='assets.Computer'),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
