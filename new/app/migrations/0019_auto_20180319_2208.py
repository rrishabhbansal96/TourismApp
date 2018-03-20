# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20180319_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='best_month2',
            field=models.CharField(choices=[('jan', 'January'), ('feb', 'February'), ('mar', 'March'), ('apr', 'April'), ('may', 'May'), ('jun', 'June'), ('jul', 'July'), ('aug', 'August'), ('sept', 'September'), ('oct', 'October'), ('nov', 'November'), ('dec', 'Decemeber')], default='dec', max_length=12),
        ),
        migrations.AlterField(
            model_name='rating',
            name='best_month',
            field=models.CharField(choices=[('jan', 'January'), ('feb', 'February'), ('mar', 'March'), ('apr', 'April'), ('may', 'May'), ('jun', 'June'), ('jul', 'July'), ('aug', 'August'), ('sept', 'September'), ('oct', 'October'), ('nov', 'November'), ('dec', 'Decemeber')], default='jan', max_length=12),
        ),
    ]