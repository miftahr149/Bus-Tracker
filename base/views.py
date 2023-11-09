from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def get_index_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'base/index.html')