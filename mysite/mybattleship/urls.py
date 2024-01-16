from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path("create_game", views.create_game, name="create_game"),
    path("battlefield/<pk>", views.show_battlefield, name="show_battlefield"),
    path('game_status/<int:game_id>/', views.GameStatusView.as_view(), name='game_status'),
    path('invitation/<int:pk>/', views.accept_invitation, name='accept_invitation'),
    path('get_player1_move/', views.get_player1_move, name='get_player1_move'),
    path('number_array_view/', views.number_array_view, name='number_array_view'),
    path("battlefields", views.Battlefield_list_view.as_view(), name="battlefields_list_view"),
    path("games", views.Game_list_view.as_view(), name="Game_list_view"),
]
