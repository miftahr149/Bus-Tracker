from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from common import views as common_views

# Create your views here.
def get_map(request: HttpRequest) -> HttpResponse:
    header, footer = common_views.get_header_footer(request)
    body = render(request, 'maps.html')
    full_html = header + body + footer
    return full_html