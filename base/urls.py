from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index_view, name='index'),
    path('route/', views.get_route, name='route'),
]