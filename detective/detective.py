#főoldal ami kapcsolatba lépjen a felhasználóval

from detective_user import *
from detective_state import *
from detective_logic import *

def detective_main():
#a játék fő funkciói.

    role = welcome()
    if not role:
        return

    state = GameState()

    if role == "detective":
        detective_story(state)
    elif role == "killer":
        killer_story(state)

    print("\nA játék véget ért. Az elért pontszámod: 90 /", state.get_score())
    if role == "detective":
        if state.get_score() == 90:
            print("Gratulálok a sikeres nyomozáshoz! Megtaláltad a gyilkost és az informátort és fényt derítettél az öt évvel ezelőtti bűntényre.")
        elif state.get_score() >= 70:
            print("Jól játszottál, de nem találtad meg az informátort. Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnáljuk, nem sikerült elkapnod a gyilkost.")
    elif role == "killer":
        if state.get_score() >= 65 and state.get_score() <= 90:
            print("Gratulálok! Megúsztad a lebukást! A játék véget ért.")
        elif state.get_score() >= 115:
            print("Gratulálok! Lebuktál! Azzal, hogy megmentetted a professzort, felfedted magad, így elkaptak! Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnos lebuktál! A játék véget ért.")

    new_play = retry_exit()
    if not new_play:
        return

    state = GameState()

    if new_play == "detective":
        detective_story(state)
    elif new_play == "killer":
        killer_story(state)

    print("\nA játék véget ért. Az elért pontszámod: 90 /", state.get_score())
    if new_play == "detective":
        if state.get_score() == 90:
            print("Gratulálok a sikeres nyomozáshoz! Megtaláltad a gyilkost és az informátort és fényt derítettél az öt évvel ezelőtti bűntényre.")
        elif state.get_score() >= 70:
            print("Jól játszottál, de nem találtad meg az informátort. Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnáljuk, nem sikerült elkapnod a gyilkost.")
    elif new_play == "killer":
        if state.get_score() >= 65 and state.get_score() <= 90:
            print("Gratulálok! Megúsztad a lebukást! A játék véget ért.")
        elif state.get_score() >= 115:
            print("Gratulálok! Lebuktál! Azzal, hogy megmentetted a professzort, felfedted magad, így elkaptak! Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnos lebuktál! A játék véget ért.")

detective_main()
input("\nNyomj egy gombot a kilépéshez...")