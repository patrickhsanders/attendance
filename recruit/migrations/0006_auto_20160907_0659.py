# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0005_link_recruit_resume_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='resume',
            field=models.ManyToManyField(blank=True, to='recruit.Resume'),
        ),
        migrations.AddField(
            model_name='recruit',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='recruit.Task'),
        ),
    ]
