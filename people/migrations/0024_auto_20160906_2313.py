# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0023_remove_student_links'),
        ('recruit', '0005_link_recruit_resume_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='recruit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruit.Recruit'),
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]