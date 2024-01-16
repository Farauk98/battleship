
from .models import Game, Battlefield, Move, Invitation
from .tables import Battlefield_table,Game_table, Invitation_table, Move_table
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class Battlefield_list_view(SingleTableView):
    model = Battlefield
    table_class = Battlefield_table
    template_name = 'table.html'

class Game_list_view(SingleTableView):
    model = Game
    table_class = Game_table
    template_name = 'table.html'
    def get_queryset(self):
        """
        Override to filter the queryset based on the logged-in user.
        Only games where the user is the owner of either battlefield_1 or battlefield_2 are returned.
        """
        user = self.request.user
        return Game.objects.filter(
            Q(battlefield_1__owner=user) | Q(battlefield_2__owner=user)
        )

class Move_list_view(LoginRequiredMixin,SingleTableView):
    model = Move
    queryset = Move.objects.all()
    table_class = Move_table
    template_name = 'table.html'

    def get(self,request,*args,**kwargs):
        pk =self.kwargs.get('pk')
        self.queryset=Move.objects.filter(game=pk)
        return super().get(request,*args,**kwargs)
    
class Invitation_list_view(LoginRequiredMixin,SingleTableView):
    model = Invitation
    queryset = Invitation.objects.all()
    table_class = Invitation_table
    template_name = 'table.html'

    def get_queryset(self):
        return Invitation.objects.filter(player2=self.request.user).filter(accept=False)
