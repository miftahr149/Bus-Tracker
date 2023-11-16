from django.http import JsonResponse
from django.conf import settings
import requests

import requests


def configure_route(access_token: str, start_coords: list, end_coords: list):

    url = f"https://api.mapbox.com/directions/v5/mapbox/driving/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}?geometries=geojson&access_token={access_token}"

    response = requests.get(url)
    if response.status_code != 200: 
        print(response.status_code)
        return None
    data = response.json()
    route_geometry = data['routes'][0]['geometry']
    return route_geometry