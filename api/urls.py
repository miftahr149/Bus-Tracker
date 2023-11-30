from django.urls import path
from . import views

urlpatterns = [
    path('address/', views.get_address, name='api_address')
]