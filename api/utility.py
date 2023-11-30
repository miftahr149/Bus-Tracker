import base.models as models

def setup_address_json() -> dict:
    result = {}
    address_list = models.Address.objects.all()
    
    for address in address_list:
        result[address.name] = {
            'lat': address.lat,
            'long': address.long
        } 
    
    return result