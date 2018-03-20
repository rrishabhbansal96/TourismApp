# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 13:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180316_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='coord',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='rating',
            name='time',
            field=models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(1)]),
        ),
    ]
