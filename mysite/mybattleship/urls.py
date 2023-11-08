from django.urls import path
from . import views

urlpatterns = [
    path("create_battlefield", views.create_battlefield, name="create_battlefield"),
    path("show_battlefield/<pk>", views.show_battlefield, name="show_battlefield"),
    path("random_shoot/<pk>", views.random_shoot, name="random_shoot"),
    path("games", views.Game_list_view.as_view(), name="game_list_view"),
    path("serial_create_game_with_random_strategy", views.serial_create_game_with_random_strategy, name="serial_create_game_with_random_strategy"),
    path("efficiency_of_methods", views.efficiency_of_methods, name="efficiency_of_methods"),
]
