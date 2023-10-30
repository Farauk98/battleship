from django.http import HttpResponse
from .battleship_utils import place_ship,create_battle_grid_html

def create_battle_grid(request):
    ships=[5,4,3,3,2]
    board = [[False for _ in range(10)] for _ in range(10)]
   
    for ship_length in ships:
        place_ship(board, ship_length)

    html_table = create_battle_grid_html(board)

    # Możesz wyświetlić lub zapisywać wynik w pliku HTML
    print(html_table)
    return HttpResponse(html_table)