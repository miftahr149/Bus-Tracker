from django.db import models
from django.conf import settings
import geocoder

# Create your models here.
token = settings.MAPBOX_ACCESS_TOKEN

class BussesInfo(models.Model):
    name = models.CharField(max_length=10)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

class Address(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.name, key=token)
        self.address = g.address
        self.long, self.lat = g.latlng
        return super(Address, self).save(*args, **kwargs)


