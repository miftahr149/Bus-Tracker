from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import os
from pathlib import Path

COMMON_TEMPLATES_PATH = Path().absolute().joinpath('common', 'templates')

def get_header_footer(request: HttpRequest) -> tuple[HttpResponse, HttpResponse]:
    header = render(request, get_template_path('header.html'))
    footer = render(request, get_template_path('footer.html'))
    return header, footer

def combine_content(*pages: HttpResponse) -> HttpResponse:
    result = pages[0].content
    for page in pages[1:]:
        result = result + page.content
    return result

def get_template_path(pathstr: str) -> Path:
    return COMMON_TEMPLATES_PATH.joinpath(pathstr)