# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20160416_2142'),
        ('attendance', '0003_register_forgot_to_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absent', models.ManyToManyField(blank=True, related_name='_dailyattendance_absent_+', to='people.Student')),
                ('active_students', models.ManyToManyField(blank=True, related_name='_dailyattendance_active_students_+', to='people.Student')),
                ('present', models.ManyToManyField(blank=True, related_name='_dailyattendance_present_+', to='people.Student')),
                ('registers', models.ManyToManyField(blank=True, to='attendance.Register')),
            ],
        ),
    ]