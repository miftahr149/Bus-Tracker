from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import os
from pathlib import Path

COMMON_TEMPLATES_PATH = 'C://Users//mifta//OneDrive//Documents//Github//Bus-Tracker//common//templates'

def get_header_footer(request: HttpRequest) -> tuple[HttpResponse, HttpResponse]:
    header = render(request, f'{COMMON_TEMPLATES_PATH}/header.html')
    footer = render(request, f'{COMMON_TEMPLATES_PATH}/footer.html')
    return header, footer

def combine_content(*pages: HttpResponse) -> HttpResponse:
    result = pages[0].content
    for page in pages[1:]:
        result = result + page.content
    return result