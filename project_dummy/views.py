from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from base import models as base_models
from . import models

# Create your views here.
def get_test_view(request: HttpRequest) -> HttpResponse:
    test = base_models.BusInfo.objects.get(name='A2')
    test = test.operation_hour.all()

    print(test)
    
    context = {
        'test': test
    }

    return render(request, 'project_dummy/index.html', context)

def get_song_list_view(
    request: HttpRequest, 
    pk: str) -> HttpResponse:

    list_song = models.ListSong.objects.get(id=int(pk))

    context = {
        'list_song': list_song.list_song.all()
    }

    return render(request, 'project_dummy/song_list.html', context)