from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_test_view, name='test'),
    path('test2/<str:bus_name>/',
         views.get_test2_view, 
         name='test2'),
    path('test3', views.get_test3_view, name='test3')
]