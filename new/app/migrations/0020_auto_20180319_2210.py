# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20180319_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='best_time',
            field=models.CharField(choices=[('morning', 'Morning'), ('day', 'Day'), ('evening', 'Evening'), ('night', 'Night')], default='day', max_length=8),
        ),
    ]
