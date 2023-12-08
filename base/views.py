from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.conf import settings
from django.views.generic.edit import CreateView
from . import models
import geocoder
import requests
from . import utility

# Create your views here.
mapbox_access_token = settings.MAPBOX_ACCESS_TOKEN

def get_index_view(request: HttpRequest, addition_context: dict=None) -> HttpResponse:
    context = {
        'mapbox_access_token': mapbox_access_token
    }
    
    if addition_context:
        context.update(addition_context)
    
    return render(request, 'base/index.html', context)

def get_route(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET': return HttpResponse()
    
    # Get current place and destination address
    current_place_address = request.GET.get('current_place')
    destination_address = request.GET.get('destination')

    # Get the lattitude and longitude
    current_place_latlng = geocoder.mapbox(current_place_address, key=mapbox_access_token).latlng
    destination_latlng = geocoder.mapbox(destination_address, key=mapbox_access_token).latlng

    context = {
        'operation': 'route',
        'current_place': current_place_latlng,
        'destination': destination_latlng
    }

    return get_index_view(request, context)
    