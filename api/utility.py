import base.models as models
from django.http import JsonResponse


def setup_address_json() -> dict:
    result = {}
    address_list = models.Address.objects.all()

    for address in address_list:
        result[address.name] = {
            'lat': address.lat,
            'long': address.long
        }

    return result


def setup_route_json(bus_type: str) -> dict:
    result = {}
    bus_route = models.BusRoute.objects.get(type_bus=bus_type)
    bus_route = bus_route.route.all()

    for pointer_address in bus_route:
        address = pointer_address.address
        result[address.name] = {
            'lat': address.lat,
            'long': address.long
        }

    return result


def setup_all_route_json() -> dict:
    result = {}
    bus_route_list = models.BusRoute.objects.all()
    for bus_route in bus_route_list:
        bus_type = bus_route.type_bus
        result[bus_type] = setup_route_json(bus_type)

    return result


def set_latlng_bus(
        bus_name: str,
        latlng: str) -> JsonResponse:

    bus_info_object = models.BusInfo.objects.get(name=bus_name)

    lat, long = latlng.split(',')
    bus_info_object.latitude = lat
    bus_info_object.longitude = long
    bus_info_object.save()

    return JsonResponse({
        'status': 'success'
    })
