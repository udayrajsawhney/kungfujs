# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MacroSensors',
            new_name='MacroSensor',
        ),
        migrations.RenameModel(
            old_name='MicroSensors',
            new_name='MicroSensor',
        ),
    ]