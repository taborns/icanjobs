# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0035_auto_20190515_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobalert',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]