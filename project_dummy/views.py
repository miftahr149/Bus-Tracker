from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from base import models as base_models
from django.conf import settings
from . import models

# Create your views here.
def get_test_view(request: HttpRequest) -> HttpResponse:
    bus_info_list = base_models.BusInfo.objects.all()

    print(bus_info_list)
    
    context = {
        'mapbox_access_token': settings.MAPBOX_ACCESS_TOKEN,
        'bus_info_list': bus_info_list
    }

    return render(request, 'project_dummy/index.html', context)

def get_test2_view(request: HttpRequest, bus_name: str) -> HttpResponse:
    bus_info = base_models.BusInfo.objects.get(name=bus_name)
    operation_hour = bus_info.operation_hour.all() 

    context = {
        'name': bus_name,
        'operation_hour': operation_hour
    }

    return render(request, 'project_dummy/test2.html', context)

def get_test3_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'project_dummy/test3.html')