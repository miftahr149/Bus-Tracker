from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.views.generic.edit import CreateView
from .models import Address

# Create your views here.
def get_index_view(request: HttpRequest) -> HttpResponse:
    mapbox_access_token = settings.MAPBOX_ACCESS_TOKEN
    center_point = Address.objects.get(name="Arked Meranti")
    return render(
        request=request, 
        template_name='base/index.html', 
        context={
            'mapbox_access_token': mapbox_access_token,
            'arked_meranti_lat': center_point.lat,
            'arked_meranti_long': center_point.long
        }
    )
    