from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
<<<<<<< HEAD
import geocoder
from base.views import mapbox_access_token
from base import models

# Create your views here.

def setup_route_json(bus_type: str) -> dict:
    result = {}
    bus_route = models.BusRoute.objects.get(type_bus=bus_type)
    bus_route = bus_route.route.all()

    for pointer_address in bus_route:
        address = pointer_address.address
        result[address.name] = {
            'lat': address.lat,
            'long': address.long
        }
    
    return result


def get_address(request: HttpRequest) -> JsonResponse:
    result = {}
    address_list = models.Address.objects.all()

    for address in address_list:
        result[address.name] = {
            'lat': address.lat,
            'long': address.long
        }

    return JsonResponse(result)
=======
from . import utility as util

# Create your views here.


def get_address(request: HttpRequest) -> JsonResponse:
    return JsonResponse(util.setup_address_json())
>>>>>>> main


def get_route(
        request: HttpRequest,
        bus_type: str) -> JsonResponse:
<<<<<<< HEAD
    
    return JsonResponse(setup_route_json(bus_type))


def get_all_route(request: HttpRequest) -> JsonResponse:
    result = {}
    bus_route_list = models.BusRoute.objects.all()
    for bus_route in bus_route_list:
        bus_type = bus_route.type_bus
        result[bus_type] = setup_route_json(bus_type)

    return JsonResponse(result)
=======
    return JsonResponse(util.setup_route_json(bus_type))


def get_all_route(request: HttpRequest) -> JsonResponse:
    return JsonResponse(util.setup_all_route_json())
>>>>>>> main


def set_latlng_bus(
        request:HttpRequest,
        bus_name:str,
        latlng:str) -> JsonResponse:
<<<<<<< HEAD
    
    bus_info_object = models.BusInfo.objects.get(name=bus_name)

    lat, long = latlng.split(',')
    bus_info_object.latitude = lat
    bus_info_object.longitude = long
    bus_info_object.save()

    return JsonResponse({
        'status': 'success'
    })

def get_geocoding(request: HttpRequest, address: str) -> JsonResponse:
    coords = geocoder.mapbox(address, key=mapbox_access_token).latlng
    return JsonResponse({'coordinate': coords})
=======
    return util.set_latlng_bus(bus_name, latlng)
>>>>>>> main
