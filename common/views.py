from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

COMMON_TEMPLATES_URL = 'common/templates'

def get_header_footer(request: HttpRequest) -> tuple[HttpResponse, HttpResponse]:
    header = render(request, f'{COMMON_TEMPLATES_URL}/header.html')
    footer = render(request, f'{COMMON_TEMPALTES_URL}/footer.html')
    return header, footer