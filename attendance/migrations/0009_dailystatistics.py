# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_remove_register_current_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average_checkin', models.DateTimeField(blank=True)),
                ('average_checkin_count', models.IntegerField(blank=True)),
                ('average_hours_spent', models.FloatField(blank=True)),
                ('average_hours_spent_count', models.IntegerField(blank=True)),
                ('percent_students_present', models.FloatField(blank=True)),
            ],
        ),
    ]
