from django.urls import path
from . import views
from . import views_table

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('login/', views.user_login, name='login'),
    path("battlefield/<pk>", views.show_battlefield, name="show_battlefield"),
    path('game_status/<int:game_id>/', views.GameStatusView.as_view(), name='game_status'),
    path('invitation_accept/<int:pk>/', views.accept_invitation, name='accept_invitation'),
    path('get_player1_move/', views.get_player1_move, name='get_player1_move'),
    path('create_invitation/', views.create_invitation, name='create_invitation'),
    path("battlefields", views_table.Battlefield_list_view.as_view(), name="battlefields_list_view"),
    path("games", views_table.Game_list_view.as_view(), name="Game_list_view"),
    path("moves/game/<int:pk>/", views_table.Move_list_view.as_view(), name="Move_list_view"),
    path("invitations", views_table.Invitation_list_view.as_view(), name="Invitation_list_view"),
]
