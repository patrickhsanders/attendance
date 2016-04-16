# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0003_auto_20160222_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frond', models.CharField(choices=[('west', 'West - Near Kitchen'), ('middle', 'Middle'), ('east', 'East'), ('windows', 'Window adjacent')], max_length=31)),
                ('seat', models.IntegerField(help_text='Northmost seat is 1, increasing clockwise from there')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Student')),
            ],
        ),
    ]
