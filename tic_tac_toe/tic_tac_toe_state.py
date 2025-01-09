def initialize_game_state():
    # Inicializálja a játék állapotát.(beállítjuk a játék elején szükséges kezdőértékeket.)
    board = [' '] * 9  # 3x3 tábla, 9 üres mezővel
    current_player = 'X'  # Kezdő játékost megadjuk
    return board, current_player  # Visszatér a board és kezdő játékos értékével


"""def print_board(board):
    # Játék tábla megjelenítése
    for i in range(0, 9, 3):  # 0-tól 8-ig lépkedünk 3 lépésenként
        print(board[i], "|", board[i+1], "|", board[i+2])  # Kiírjuk a sorokat
        if i < 6:  # Csak akkor nyomunk sortörést, ha nem az utolsó sor
            print('--------------')"""


def print_board(board):
    size = 3
    print("+" + "-" * (size * 4 - 1) + "+")

    for i in range(size):  # sorokon megy
        print("|", end=" ")
        for j in range(size):  # oszlopokon megy
            # Kiírjuk a táblát, a lista alapján
            # Azlista indexelése. Cellaérték kiszámítása
            cell = board[i * size + j]
            print(cell, end=" | ")
        print()  # Sor lezárása
        if i < size - 1:
            print("+" + "-" * (size * 4 - 1) + "+")

    print("+" + "-" * (size * 4 - 1) + "+")
