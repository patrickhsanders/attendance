# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('course', models.CharField(choices=[('ios', 'iOS Full-time'), ('android', 'Android Full-time'), ('swift', 'iOS Part-time (Swift)')], max_length=31)),
                ('description', models.TextField(blank=True, null=True)),
                ('project_file', models.FileField(blank=True, null=True, upload_to='uploads/projects')),
                ('public_link_to_project', models.URLField(blank=True, null=True)),
                ('nextProject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
