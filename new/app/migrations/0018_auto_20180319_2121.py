# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20180319_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
