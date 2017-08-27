# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_auto_20170827_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macrosensor',
            name='Humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='macrosensor',
            name='WaterLevel',
            field=models.FloatField(null=True),
        ),
    ]
