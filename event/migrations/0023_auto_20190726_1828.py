# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-26 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_blog_is_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
