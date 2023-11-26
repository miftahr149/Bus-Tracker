from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.BusInfo)
admin.site.register(models.OperationHour)
admin.site.register(models.BusOperationHour)