from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def get_map(request: HttpRequest) -> HttpResponse:
    return render(request, 'maps.html')