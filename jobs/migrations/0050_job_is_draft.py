# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-07 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0049_auto_20190528_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
