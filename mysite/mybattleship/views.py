from django.http import HttpResponse
from .battleship_utils import place_ship,create_battle_grid_html, random_method, create_game
from .models import Game,Battle_grid, Move
from django.shortcuts import get_object_or_404, redirect
from .tables import Game_table
from django_tables2 import SingleTableView
import random
import time
from django.db.models import Avg

def create_battlefield(request):
    _,board = create_game()
    html_table = create_battle_grid_html(board)
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
        random_method(game)
    elif game.score != 0:
        counter =  game.score
    return HttpResponse(counter)
    
def serial_create_game_with_random_strategy(request):
    total_time = 0
    num_iterations = 100
    for _ in range(num_iterations):
        start_time = time.time()
        game,board = create_game()
        random_method(game)
        end_time = time.time()  # Czas po zakończeniu kroku
        step_time = end_time - start_time  # Czas trwania kroku
        total_time += step_time

    average_step_time = total_time / num_iterations
    response_text = f"Average time for one step: {average_step_time} seconds"
    return HttpResponse(response_text)

def serial_create_game_with_random_strategy(request):
    total_time = 0
    num_iterations = 100
    for _ in range(num_iterations):
        start_time = time.time()
        game,board = create_game()
        random_method(game)
        end_time = time.time()  # Czas po zakończeniu kroku
        step_time = end_time - start_time  # Czas trwania kroku
        total_time += step_time

    average_step_time = total_time / num_iterations
    response_text = f"Average time for one step: {average_step_time} seconds"
    return HttpResponse(response_text)

def efficiency_of_methods(request):
    avg_score = Game.objects.aggregate(avg_score=Avg('score'))['avg_score']
    response_text = f"Average efficiency_of_methods: {avg_score}"
    return HttpResponse(response_text)

