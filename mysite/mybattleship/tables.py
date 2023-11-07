import django_tables2 as tables
from .models import Game

class Game_table(tables.Table):
    show_battlefield = tables.LinkColumn(
        verbose_name="Battlefield",
        text="Show",  
        viewname="show_battlefield",  
        args=[tables.A("id")]
    )
    class Meta:
        model = Game
        template_name = "django_tables2/bootstrap.html"
        fields = ("id","score" )