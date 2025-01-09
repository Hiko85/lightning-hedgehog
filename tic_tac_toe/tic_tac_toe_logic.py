from tic_tac_toe_state import initialize_game_state, print_board
from tic_tac_toe_user import *


def starting(scores):
    # Inicializáljuk a játék állapotát
    board, current_player = initialize_game_state()
    winner = None  # Inicializáljuk a győztes változót

    # Ellenőrizzük tele van e tábla éa a győztest is
    while not is_board_full(board) and winner is None:
        print_board(board)  # Tábla megjelenítése

        move = get_player_move(current_player)  # Kéri a játékostól a lépést

        # Ellenőrizzük, hogy a mező szabad-e
        if board[move] == ' ':  # ha mező szabad
            board[move] = current_player  # current player odalép
            winner = check_winner(board)  # Ellenőrizzük a győztest

            # Váltás a következő játékosra, ha nincs győztes
            if winner is None:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Ez a mező már foglalt. Próbálj újra.")  # Ha a mező foglalt

    # Játék vége, győztes vagy döntetlen
    print_board(board)  # Tábla megjelenítése a játék végén

    if winner:
        display_winner(winner)  # Megjeleníti győztes üzenetet
        scores[winner] += 1  # Frissítjük a győztes pontszámát
    else:
        display_draw()  # Megjeleníti a döntetlen üzenetet

    # Pontszámok megjelenítése
    print(f"Pontszámok: X: {scores['X']}, O: {scores['O']}")


def check_winner(board):  # van e nyertes
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Sorok
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Oszlopok
        [0, 4, 8], [2, 4, 6]              # Átlók
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None

# függvény megvizsgálja, hogy a táblában nincs-e szóköz (' '), ami az üres mezőtképezi.
# board változó, egy lista ami a játék mezőit tartalmazza. = játék tábla reprezentációja


def is_board_full(board):
    return ' ' not in board
