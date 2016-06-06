# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_dailystatistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystatistics',
            name='average_checkin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='average_checkin_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='average_hours_spent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='average_hours_spent_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatistics',
            name='percent_students_present',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
