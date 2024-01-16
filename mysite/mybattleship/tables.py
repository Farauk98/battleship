import django_tables2 as tables
from .models import Battlefield,Game

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
        fields = ("id", 'owner')

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
    class Meta:
        model = Game
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", 'battlefield_1','battlefield_1.owner','battlefield_2','battlefield_2.owner','winner')