# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-08 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_auto_20190308_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeejobinterest',
            name='job_level',
        ),
        migrations.AddField(
            model_name='employeejobinterest',
            name='job_level',
            field=models.ManyToManyField(to='jobs.JobLevel'),
        ),
    ]
