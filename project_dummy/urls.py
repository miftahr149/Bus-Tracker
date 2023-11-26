from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_test_view, name='test'),
    path('song_list/<str:pk>/',
         views.get_song_list_view, 
         name='song_list')
]