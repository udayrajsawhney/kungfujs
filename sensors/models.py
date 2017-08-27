# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class MacroSensor(models.Model):
    read_time = models.DateField(auto_now=True)
    Temperature = models.FloatField()
    Humidity = models.FloatField(null = True)
    WaterLevel = models.FloatField(null = True)

    def __str__(self):
        return 'Temperature ' + str(self.Temperature) + 'C - Humidity' + str(self.Humidity) + '% - WaterLevel' + str(self.WaterLevel) + 'cm'

class addPlant(models.Model):
    SoilMoisture = models.FloatField()

    def __str__(self):
        return 'SoilMoisture' + str(self.SoilMoisture)


class MicroSensor(models.Model):
    plant=models.ForeignKey(addPlant,on_delete=models.CASCADE)
