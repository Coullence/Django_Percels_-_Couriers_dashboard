# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import itemModel, stationModel, paymentModel, smsModel

admin.site.register([itemModel, stationModel, paymentModel, smsModel])
