# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_appointment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[(b'read', b'Seen'), (b'unread', b'Not Seen')], default='unread', max_length=10),
        ),
    ]
