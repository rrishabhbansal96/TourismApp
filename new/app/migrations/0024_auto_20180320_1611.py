# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='question',
            field=models.CharField(default='', max_length=1000),
        ),
    ]