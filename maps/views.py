from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from common import utility as utils

# Create your views here.
def get_map(request: HttpRequest) -> HttpResponse:
    header, footer = utils.get_header_footer(request)
    body = render(request, 'maps.html')
    combine_html = utils.combine_content(header, body, footer)
    return HttpResponse(combine_html)

def test_func(request: HttpRequest) -> HttpResponse:
    header, footer = common_views.get_header_footer(request)
    body = render(request, 'maps.html')
    full_html = header + body + footer
    return full_html