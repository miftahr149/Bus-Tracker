from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from . import utility as util

# Create your views here.

def get_address(request: HttpRequest) -> JsonResponse:
    return JsonResponse(util.setup_address_json())