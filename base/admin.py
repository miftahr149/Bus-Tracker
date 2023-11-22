from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.BusInfo)
admin.site.register(models.Address)
admin.site.register(models.BusRoute)
admin.site.register(models.OperationHour)