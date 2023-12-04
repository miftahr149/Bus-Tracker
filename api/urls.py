from django.urls import path
from . import views

urlpatterns = [
    path('address/', views.get_address, name='api_address'),
    path('route/<str:bus_type>/', views.get_route, name='api_route'),
    path('route/', views.get_all_route, name='api_route_all'),
    path('set_latlng/<str:bus_name>/<str:latlng>', 
        views.set_latlng_bus, 
<<<<<<< HEAD
        name='api_set_latlng'),
    path('geocoding/<str:address>', views.get_geocoding, name='api_geocoding')
=======
        name='set_latlng')
>>>>>>> main
]