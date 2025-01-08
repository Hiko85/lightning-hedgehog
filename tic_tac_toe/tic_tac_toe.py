from tic_tac_toe_logic import check_winner, is_board_full, starting
from tic_tac_toe_user import get_player_move, display_winner, display_draw, welcome
# Importáljuk a globális változókat és a print_board függvényt
from tic_tac_toe_state import initialize_game_state, print_board


def main():
    welcome()

    choice = ""
    while choice != "2":
        print("1. Játék indítás")
        print("2. Kilépés")

        choice = input("Add meg a választásod (1-2): ").strip()

        if choice == "1":
            print("\nIndul a játék!\n")
            starting()
        if choice == "2":
            print("\nKöszönjük!\n")


if __name__ == "__main__":
    main()
