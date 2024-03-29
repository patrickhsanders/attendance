# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_student_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalinformation',
            name='incoming_level',
        ),
        migrations.AlterField(
            model_name='educationalexperience',
            name='degree',
            field=models.CharField(choices=[('hs', 'High School Diploma or Equivalent'), ('aa', "Associate's Degree"), ('ba', "Bachelor's Degree"), ('ma', "Master's Degree"), ('mba', 'MBA'), ('phd', 'Doctor of Philosophy'), ('other', 'Other')], max_length=7),
        ),
        migrations.AlterField(
            model_name='educationalexperience',
            name='end_date',
            field=models.IntegerField(blank=True, choices=[(2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980)]),
        ),
        migrations.AlterField(
            model_name='educationalexperience',
            name='start_date',
            field=models.IntegerField(blank=True, choices=[(2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980)]),
        ),
        migrations.AlterField(
            model_name='educationalinformation',
            name='has_cs_degree',
            field=models.BooleanField(default=False, verbose_name='Check this if you have a CS degree.'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uses_own_laptop',
            field=models.BooleanField(default=True, verbose_name='I am using my own laptop.'),
        ),
    ]
