from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect,render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from .models import Game, Battlefield,Battle_grid, Move, User, Invitation
from .forms import ShotForm, UserLoginForm, CreateInvitationForm
from .battleship_utils import create_game_for_one, create_battle_grid_html

from .models import ChatMessage
from .forms import ChatForm

def main_menu(request):
    return render(request, 'main_menu.html')

class GameStatusView(TemplateView):
    template_name = 'game_status.html'

    def post(self, request, *args, **kwargs):
        game_id = kwargs.get('game_id')
        game = get_object_or_404(Game, id=game_id)
        if 'submit_chat' in request.POST:
            # Handle chat form submission
            chat_form = ChatForm(request.POST)
            if chat_form.is_valid():
                new_message = chat_form.save(commit=False)
                new_message.game = game
                new_message.sender = request.user
                new_message.save()
        elif 'submit_shot' in request.POST:

            form = ShotForm(request.POST)
            user = self.request.user
            game_id = kwargs.get('game_id')
            game = get_object_or_404(Game, id=game_id)
            if form.is_valid():
                x = form.cleaned_data['x']
                y = form.cleaned_data['y']
                if user == game.battlefield_1.owner: 
                    opponent_battlefield = game.battlefield_2
                elif user == game.battlefield_2.owner:
                    opponent_battlefield = game.battlefield_1

                else:
                    return redirect('error')
            
                battle_grid = Battle_grid.objects.get(
                    battlefield = opponent_battlefield,
                    x = x ,
                    y = y ,
                )
                if not battle_grid.is_shot:
                    try:
                        order = Move.objects.filter(game=game).latest('order').order + 1
                    except:
                        order = 1

                    move = Move(
                        game = game,
                        battle_grid = battle_grid,
                        order =order
                        
                    )
                    move.save()
                    battle_grid.is_shot = True
                    battle_grid.save()

                    game.player1_move = not game.player1_move
                    game.save()

                    check_if_win = Battle_grid.objects.filter(battlefield = opponent_battlefield).filter(is_ship=True).filter(is_shot=False)
                    if len(check_if_win) == 0:
                        game.winner = user
                        game.score = order
                        game.save()
                        return HttpResponse("Wygrales")
                    else:
                        return redirect('game_status', game_id=kwargs.get('game_id'))  # Przekieruj z powrotem do widoku gry
                else:
                    request.session['shot_error'] = "This grid has already been shot at."
                return redirect('game_status', game_id=game_id)


        # W przypadku błędów formularza, przekieruj z powrotem z informacją o błędzie
        return redirect('game_status', game_id=kwargs.get('game_id'))

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check for shot error message
        if 'shot_error' in request.session:
            context['shot_error'] = request.session['shot_error']
            del request.session['shot_error']  # Clear the message after retrieving it

        user = self.request.user
        # Stan gry
        game_id = kwargs.get('game_id')
        game = get_object_or_404(Game, id=game_id)


        if user == game.battlefield_1.owner: 
            player_battlefield = game.battlefield_1
            opponent_battlefield = game.battlefield_2
            player = 1
        elif user == game.battlefield_2.owner:
            player_battlefield = game.battlefield_2
            opponent_battlefield = game.battlefield_1
            player = 2
        else:
            return HttpResponse("Nie masz dostepu do tej sekcji")
        if game.winner is None:
            context['winner'] =  True
        else:
            context['winner'] =  False

        context['player1_move'] = game.player1_move
        if (player==1 & game.player1_move) or ((player==2) &  (game.player1_move==False)):
            context['your_turn'] = True 
        else:
            context['your_turn'] = False 

        context['game_id'] = game_id

        context['user'] = user
        
        # Przetwarzanie bitew
        board = self.process_own_battlefield(player_battlefield)
        context['html_table1'] = create_battle_grid_html(board)


        board2 = self.process_opponent_battlefield(game, opponent_battlefield)
        context['html_table2'] = create_battle_grid_html(board2)

        moves = Move.objects.filter(game= game)
  
        context['moves'] = moves

        context['shot_form'] = ShotForm()

        game_id = kwargs.get('game_id')
        context['chat_messages'] = ChatMessage.objects.filter(game_id=game_id).order_by('-timestamp')[:10]  # last 10 messages
        context['chat_form'] = ChatForm()

        return render(request, self.template_name, context)

    
    def process_own_battlefield(self, battlefield):
        board = [[[False, False] for _ in range(10)] for _ in range(10)]

        battle_grids_ship = Battle_grid.objects.filter(battlefield=battlefield, is_ship=True)
        for grid in battle_grids_ship:
            board[grid.x][grid.y][0] = True

        battle_grids_shot = Battle_grid.objects.filter(battlefield=battlefield, is_shot=True)
        for grid in battle_grids_shot:
            board[grid.x][grid.y][1] = True

        return board
    
    def process_opponent_battlefield(self,game,battlefield):
        board = [[[False, False] for _ in range(10)] for _ in range(10)]

        moves = Move.objects.filter(game=game).filter(battle_grid__battlefield_id = battlefield)

        for move in moves:
            if move.battle_grid.is_ship:
                board[move.battle_grid.x][move.battle_grid.y][0] = True
            board[move.battle_grid.x][move.battle_grid.y][1] = True
        return board

def get_player1_move(request):
    game = Game.objects.first()  # Assuming you have only one game for simplicity
    data = {'player1_move': game.player1_move}
    return JsonResponse(data)

def accept_invitation(request,pk):
    invitation = get_object_or_404(Invitation, id=pk)
    if request.user == invitation.player2:


        invitation.accept = True
        invitation.save()

        battlefield_1= create_game_for_one(player = invitation.player1, ships = invitation.ships_sizes)
        battlefield_2= create_game_for_one(player = invitation.player2, ships = invitation.ships_sizes)
        game = Game(
            score = 0,
            battlefield_1 = battlefield_1,
            battlefield_2 = battlefield_2
        )
        game.save()
        
        return redirect('game_status',game.id )

    else:
        return HttpResponse("Nie masz dostepu do tego zaproszenia")

def show_battlefield(request,pk):
    battlefield = get_object_or_404(Battlefield, id=pk)
    board = [[[False,False] for _ in range(10)] for _ in range(10)]
    array_of_battle_grids = Battle_grid.objects.filter(battlefield = battlefield).filter(is_ship = True)
    for battle_grid in array_of_battle_grids:
        board[battle_grid.x][battle_grid.y][0] = True
    array_of_battle_grids = Battle_grid.objects.filter(battlefield = battlefield).filter(is_shot = True)
    for battle_grid in array_of_battle_grids:
        board[battle_grid.x][battle_grid.y][1] = True
    html_table = create_battle_grid_html(board)

    # Możesz wyświetlić lub zapisywać wynik w pliku HTML
    return HttpResponse(html_table)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_menu')  # Zastąp 'home' odpowiednim adresem URL
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def create_invitation(request):
    # Initialize the form with the current queryset excluding the current user
    form = CreateInvitationForm(request.user)
    if request.method == 'POST':
        # Pass the current user to the form for POST request as well
        form = CreateInvitationForm(request.user, request.POST)
        if form.is_valid():
            numbers = form.cleaned_data['numbers']
            user2 = form.cleaned_data['user']
            
            invitation = Invitation(
                player1 = request.user,
                player2 = user2,
                ships_sizes = numbers
            )

            invitation.save()
            return HttpResponse("Created")
    else:
        form = CreateInvitationForm(request.user)

    return render(request, 'number_array_template.html', {'form': form})

