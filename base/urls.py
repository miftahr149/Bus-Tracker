from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index_view, name='index'),
    path('route/', views.get_route, name='route'),
    path('test/', views.get_test, name='test')
]