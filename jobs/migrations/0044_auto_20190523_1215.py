# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 12:15
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0043_auto_20190523_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='salary_unpaid',
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]