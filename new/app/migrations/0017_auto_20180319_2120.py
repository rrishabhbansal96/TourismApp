# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20180319_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='best_month',
            field=models.CharField(choices=[('jan', 'January'), ('feb', 'February'), ('mar', 'March'), ('apr', 'April'), ('may', 'May'), ('jun', 'June'), ('jul', 'July'), ('aug', 'August'), ('sept', 'September'), ('oct', 'October'), ('nov', 'November'), ('dec', 'Decemeber'), ('evr', 'Every Month')], default='evr', max_length=12),
        ),
    ]
