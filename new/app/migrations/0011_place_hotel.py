# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180319_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='hotel',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
