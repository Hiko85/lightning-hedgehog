
def print_board(board):
    # Játék tábla megjelenítése.
    for i in range(3):
        print(' | '.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-----')


def welcome():
    print("Üdvözöllek az amőba játékban")


def get_player_move(player):
    move = 0
    while move < 1 or move > 9:  # Végig most egy érvényes számot keresünk
        # Beolvasás
        move = int(input(f"Player {player}, válassz egy mezőt (1-9): "))

        if move < 1 or move > 9:  # Ha a bemenet nem az elvárt tartományban van
            print("Kérlek, adj meg egy számot 1 és 9 között.")  # Hibaüzenet

    return move - 1  # Érvényes bemenet esetén visszaadjuk a 0-alapú indexet


def display_winner(player):
    # Megjeleníti a győztes üzenetet.
    print(f"Player {player} nyert!")


def display_draw():
    # Megjeleníti a döntetlen üzenetet.
    print("Döntetlen!")
