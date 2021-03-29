from django.urls import path
from . import views

app_name='webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('player_directory', views.player_directory, name='player_directory'),
    path('create_a_formation', views.create_a_formation, name='create_a_formation'),
    path('create_a_formation/player_register', views.player_register, name='player_register'),
    path('upload', views.upload, name='upload'),
]