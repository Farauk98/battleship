from django.urls import path
from . import views

urlpatterns = [
    path("create_battlefield", views.create_battlefield, name="create_battlefield"),
    path("show_battlefield/<pk>", views.show_battlefield, name="show_battlefield"),
    path("random_shoot/<pk>", views.random_shoot, name="random_shoot"),
    path("games", views.Game_list_view.as_view(), name="game_list_view"),
]
