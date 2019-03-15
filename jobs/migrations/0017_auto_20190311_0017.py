# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 00:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jobs.functions


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_auto_20190310_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
        migrations.AlterField(
            model_name='employee',
            name='about_me',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='applications',
            field=models.ManyToManyField(blank=True, related_name='applicants', through='jobs.JobApplication', to='jobs.Job'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.FileField(blank=True, upload_to=jobs.functions.getFileName),
        ),
        migrations.AlterField(
            model_name='employee',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Region'),
        ),
        migrations.AlterField(
            model_name='employeejobinterest',
            name='pay_period',
            field=models.CharField(choices=[(b'year', b'Per Year'), (b'month', b'Per Month'), (b'day', b'Per Day'), (b'hour', b'Per Hour')], max_length=10),
        ),
    ]
