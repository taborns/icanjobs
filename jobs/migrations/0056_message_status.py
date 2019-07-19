# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-10 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0055_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[(b'read', b'Seen'), (b'unread', b'Not Seen')], default='unread', max_length=10),
        ),
    ]