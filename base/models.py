from django.db import models
from django.conf import settings
import geocoder
import datetime
from django.db.models import F

# Create your models here.
token = settings.MAPBOX_ACCESS_TOKEN


class Address(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    get_latlong = models.BooleanField(
        default=False, verbose_name="Automatic Get Address")

    def save(self, *args, **kwargs):
        if not self.get_latlong:
            return super(Address, self).save(*args, **kwargs)
        g = geocoder.mapbox(self.name, key=token)
        self.address = g.address
        self.lat, self.long = g.latlng
        return super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class StartRoute(models.Model):
    for_bus_route = models.CharField(max_length=20)
    route = models.ManyToManyField(Address)

    class Meta:
        ordering = ['for_bus_route']

    def __str__(self) -> str:
        return self.for_bus_route


class EndRoute(models.Model):
    for_bus_route = models.CharField(max_length=20)
    route = models.ManyToManyField(Address)

    def __str__(self) -> str:
        return self.for_bus_route


class BusRoute(models.Model):
    type_bus = models.CharField(max_length=20)
    route_start = models.ForeignKey(
        StartRoute, on_delete=models.CASCADE, null=True)
    round_end = models.ForeignKey(
        EndRoute, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type_bus


class OperationHour(models.Model):
    start = models.TimeField(blank=True, null=True, default=datetime.time())
    end = models.TimeField(blank=True, null=True)

    start_break = models.BooleanField(default=False)
    end_break = models.BooleanField(default=False)

    class Meta:
        ordering = ['start', 'end']

    def __str__(self):
        start = 'Break'
        end = 'Break'
        
        if not self.start_break and self.start is not None :
            start = self.start.strftime("%H:%M")

        if not self.end_break and self.end is not None:
            end = self.end.strftime("%H:%M")

        return f'{start} - {end}'


class BusInfo(models.Model):
    name = models.CharField(max_length=20)
    bus_route = models.ForeignKey(
        BusRoute, on_delete=models.CASCADE)
    operation_hour = models.ManyToManyField(OperationHour)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    weekend = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
