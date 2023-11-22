from django.db import models
from django.conf import settings
import geocoder
import datetime

# Create your models here.
token = settings.MAPBOX_ACCESS_TOKEN

def hour_to_minute(datetime_object: datetime.time):
    return (60 * datetime_object.hour) + datetime_object.minute

def minute_to_hour(total_minute: int):
    minute = total_minute % 60
    hour = int((total_minute - minute) / 60)
    return hour, minute

class Address(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    get_latlong = models.BooleanField(default=False, verbose_name="Automatic Get Address")

    def save(self, *args, **kwargs):
        if not self.get_latlong: return super(Address, self).save(*args, **kwargs)
        g = geocoder.mapbox(self.name, key=token)
        self.address = g.address
        self.lat, self.long = g.latlng
        return super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class BusRoute(models.Model):
    type_bus = models.CharField(max_length=3)
    route = models.ManyToManyField(Address)

    def __str__(self):
        return self.type_bus

class OperationHour(models.Model):
    start = models.TimeField()
    end = models.TimeField(blank=True)

    def save(self, *args, **kwargs):
        total_minute = hour_to_minute(self.start)
        hour, minute = minute_to_hour(total_minute + 15)
        self.end = datetime.time(hour=hour, minute=minute)
        return super(OperationHour, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.start

class BusInfo(models.Model):
    name = models.CharField(max_length=3)
    bus_route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    operation_hour = models.ForeignKey(OperationHour, on_delete=models.CASCADE)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    weekend = models.BooleanField(default=False)

    def __str__(self):
        return self.name