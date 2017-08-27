# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MacroSensor,addPlant

admin.site.register(addPlant)
admin.site.register(MacroSensor)

