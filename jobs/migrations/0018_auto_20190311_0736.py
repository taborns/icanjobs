# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20190311_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeejobinterest',
            name='employement_types',
        ),
        migrations.RemoveField(
            model_name='employeejobinterest',
            name='job_categories',
        ),
        migrations.RemoveField(
            model_name='employeejobinterest',
            name='job_levels',
        ),
        migrations.RemoveField(
            model_name='employeejobinterest',
            name='job_regions',
        ),
        migrations.AddField(
            model_name='employeejobinterest',
            name='employement_type',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.EmployementType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeejobinterest',
            name='job_category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeejobinterest',
            name='job_level',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.JobLevel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeejobinterest',
            name='job_region',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Region'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employeejobinterest',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preference', to='jobs.Employee'),
        ),
        migrations.AlterField(
            model_name='employeejobinterest',
            name='pay_period',
            field=models.CharField(blank=True, choices=[(b'year', b'Per Year'), (b'month', b'Per Month'), (b'day', b'Per Day'), (b'hour', b'Per Hour')], max_length=10),
        ),
        migrations.AlterField(
            model_name='employeejobinterest',
            name='salary_end',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='employeejobinterest',
            name='salary_start',
            field=models.IntegerField(blank=True),
        ),
    ]
