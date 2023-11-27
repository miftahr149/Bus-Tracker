from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from base import models as base_models
from . import models

# Create your views here.
def get_test_view(request: HttpRequest) -> HttpResponse:
    bus_info_list = base_models.BusInfo.objects.all()

    print(bus_info_list)

    def create_test_context() -> list:
        result = []

        for bus_info in bus_info_list:
            bus_operation_hour_id = bus_info.operation_hour.id

            result.append({
                'name': bus_info.name,
            })

        return result
    
    context = {
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