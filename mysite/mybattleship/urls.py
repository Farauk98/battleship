from django.urls import path
from . import views

urlpatterns = [
    path("battleship", views.create_battle_grid, name="create_battle_grid"),
]
