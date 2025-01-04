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

    print("\nA játék véget ért. Az elért pontszámod:", state.get_score())
    if role == "detective":
        if state.get_score() >= 50:
            print("Gratulálunk! Sikerült elkapnod a gyilkost!")
        else:
            print("Sajnáljuk, nem sikerült elkapnod a gyilkost.")
    elif role == "killer":
        if state.get_score() >= 50:
            print("Gratulálunk! Sikerült megúsznod a bűntényt!")
        else:
            print("Elkaptak a rendőrök. A bűntett kiderült.")

detective_main()
