from django.http import HttpResponse
from .battleship_utils import place_ship,create_battle_grid_html
from .models import Game,Battle_grid, Move
from django.shortcuts import get_object_or_404
from .tables import Game_table
from django_tables2 import SingleTableView
import random

def create_battlefield(request):
    ships=[5,4,3,3,2]
    board = [[False for _ in range(10)] for _ in range(10)]
   
    for ship_length in ships:
        place_ship(board, ship_length)

    game = Game(score=0)
    game.save()
    counter_x =0
    for row in board:
        counter_y =0
        for column in row:
            battle_grid =Battle_grid(
                game = game,
                x=counter_x,
                y=counter_y,
                is_ship = column
            )
            battle_grid.save()
            counter_y+=1
        counter_x+=1

    html_table = create_battle_grid_html(board)

    # Możesz wyświetlić lub zapisywać wynik w pliku HTML
    print(html_table)
    return HttpResponse(html_table)

def show_battlefield(request,pk):
    game = get_object_or_404(Game, id=pk)
    board = [[False for _ in range(10)] for _ in range(10)]
    array_of_battle_grids = Battle_grid.objects.filter(game = game).filter(is_ship = True)
    for battle_grid in array_of_battle_grids:
        board[battle_grid.x][battle_grid.y]= True

    html_table = create_battle_grid_html(board)

    # Możesz wyświetlić lub zapisywać wynik w pliku HTML
    print(html_table)
    return HttpResponse(html_table)

class Game_list_view(SingleTableView):
    model = Game
    table_class = Game_table
    template_name = 'table.html'

def random_shoot(request,pk):
    game = get_object_or_404(Game, id=pk)
    if game.score == 0:
        array_of_battle_grids = Battle_grid.objects.filter(game = game)
        counter = 0
        while len(array_of_battle_grids.filter(is_ship=True)):
            counter += 1
            index = random.randint(0,len(array_of_battle_grids)-1)
            move = Move(
                game = game,
                battle_grid = array_of_battle_grids[index],
                order = counter
            )
            move.save()
            array_of_battle_grids = array_of_battle_grids.exclude(id = array_of_battle_grids[index].id)
        game.score = counter
        game.save()
    elif game.score != 0:
        counter =  game.score
    return HttpResponse(counter)