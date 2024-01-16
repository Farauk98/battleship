import random
from .models import Battlefield, Battle_grid, Boat, Move

# def create_battle_grid_html(board):
#     # Ustal rozmiar planszy
#     rows = len(board)
#     cols = len(board[0])

#     # Rozmiar i styl komórek
#     cell_size = "30px"
#     cell_style = "width: {0}; height: {0};".format(cell_size)

#     html = "<table border='1' style='border-collapse: collapse;'>"
#     for row in board:
#         html += "<tr>"
#         for cell in row:
#             if cell:
#                 html += "<td style='{} background-color: blue;'></td>".format(cell_style)
#             else:
#                 html += "<td style='{}'></td>".format(cell_style)
#         html += "</tr>"
#     html += "</table>"
#     return html

def create_battle_grid_html(board):
    # Ustal rozmiar planszy
    rows = len(board)
    cols = len(board[0])

    # Rozmiar i styl komórek
    cell_size = "30px"
    cell_style = "width: {0}; height: {0}; text-align: center;".format(cell_size)

    html = "<table border='1' style='border-collapse: collapse;'>"
    for row in board:
        print(row)
        html += "<tr>"
        for cell in row:
            if cell[0] and not cell[1]:
                html += "<td style='{} background-color: blue;'></td>".format(cell_style)
            elif not cell[0] and cell[1]:
                html += "<td style='{} background-color: red; color: white;'>{}</td>".format(cell_style, "X")
            elif cell[0] and cell[1]:
                html += "<td style='{} background-color: purple; color: white;'>{}</td>".format(cell_style, "X")
            else:
                html += "<td style='{}'>{}</td>".format(cell_style, "")
        html += "</tr>"
    html += "</table>"
    return html

def place_ship(board, ship_length, empty=False,fill=True):
    battle_grids =[]
    while True:
        # Wybierz losowe współrzędne początkowe statku
        start_x = random.randint(0, 9)
        start_y = random.randint(0, 9)
        orientation = random.choice(['horizontal', 'vertical'])

        # Sprawdź, czy statek może być umieszczony na planszy w wybranej orientacji
        if orientation == 'horizontal' and start_x + ship_length <= 10:
            can_place = all(board[start_x + i][start_y] == empty for i in range(ship_length))
        elif orientation == 'vertical' and start_y + ship_length <= 10:
            can_place = all(board[start_x][start_y + i] == 0 for i in range(ship_length))
        else:
            can_place = False

        # Jeśli można umieścić statek, to umieść go na planszy i wyjdź z pętli
        if can_place:
            if orientation == 'horizontal':
                for i in range(ship_length):
                    board[start_x + i][start_y] = fill
                    battle_grids.append((start_x+i,start_y))
                return battle_grids
            else:
                for i in range(ship_length):
                    board[start_x][start_y + i] = fill
                    battle_grids.append((start_x,start_y+i))
                return battle_grids
            break

def create_game_for_one(player = None,ships=[2]):
    board = [[False for _ in range(10)] for _ in range(10)]
    ships_battle_grids =[]
    for ship_length in ships:
        ships_battle_grids.append(place_ship(board, ship_length))

    battlefield = Battlefield(owner = player)
    battlefield.save()
    counter_x =0
    for row in board:
        counter_y =0
        for column in row:
            battle_grid =Battle_grid(
                battlefield = battlefield,
                x=counter_x,
                y=counter_y,
                is_ship = column
            )
            battle_grid.save()
            counter_y+=1
        counter_x+=1
    return battlefield