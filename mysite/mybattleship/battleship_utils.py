import random

def create_battle_grid_html(board):
    # Ustal rozmiar planszy
    rows = len(board)
    cols = len(board[0])

    # Rozmiar i styl komórek
    cell_size = "30px"
    cell_style = "width: {0}; height: {0};".format(cell_size)

    html = "<table border='1' style='border-collapse: collapse;'>"
    for row in board:
        html += "<tr>"
        for cell in row:
            if cell:
                html += "<td style='{} background-color: blue;'></td>".format(cell_style)
            else:
                html += "<td style='{}'></td>".format(cell_style)
        html += "</tr>"
    html += "</table>"
    return html

def place_ship(board, ship_length, empty=False,fill=True):
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
            else:
                for i in range(ship_length):
                    board[start_x][start_y + i] = fill
            break