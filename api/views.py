from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from . import utility as util

# Create your views here.


def get_address(request: HttpRequest) -> JsonResponse:
    return JsonResponse(util.setup_address_json())


def get_route(
        request: HttpRequest,
        bus_type: str) -> JsonResponse:
    return JsonResponse(util.setup_route_json(bus_type))


def get_all_route(request: HttpRequest) -> JsonResponse:
    return JsonResponse(util.setup_all_route_json())


def set_latlng_bus(
        request:HttpRequest,
        bus_name:str,
        latlng:str) -> JsonResponse:
    return util.set_latlng_bus(bus_name, latlng)
