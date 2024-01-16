import django_tables2 as tables
from .models import Battlefield,Game, Invitation

class Battlefield_table(tables.Table):
    show_battlefield = tables.LinkColumn(
        verbose_name="Battlefield",
        text="Show",  
        viewname="show_battlefield",  
        args=[tables.A("id")]
    )
    class Meta:
        model = Battlefield
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", 'owner')

class Move_table(tables.Table):
    class Meta:
        model = Battlefield
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", 'order','battle_grid')

class Invitation_table(tables.Table):
    accept_invitation = tables.LinkColumn(
        verbose_name="Invitation_accept",
        text="Accept",  
        viewname="accept_invitation",  
      args=[tables.A("id")]
    )
    class Meta:
        model = Invitation
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", 'player1','player2','ships_sizes','accept')

class Game_table(tables.Table):
    show_battlefield1 = tables.LinkColumn(
        verbose_name="Battlefield1",
        text="Show",  
        viewname="show_battlefield",  
        args=[tables.A("battlefield_1.id")]
    )

    show_battlefield2 = tables.LinkColumn(
        verbose_name="Battlefield2",
        text="Show",  
        viewname="show_battlefield",  
        args=[tables.A("battlefield_1.id")]
    )
    game = tables.LinkColumn(
        verbose_name="Game",
        text="Show",  
        viewname="game_status",  
        args=[tables.A("id")]
    )
    moves = tables.LinkColumn(
        verbose_name="Moves",
        text="Show",  
        viewname="Move_list_view",  
        args=[tables.A("id")]
    )
    class Meta:
        model = Game
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", 'battlefield_1','battlefield_1.owner','battlefield_2','battlefield_2.owner','winner')