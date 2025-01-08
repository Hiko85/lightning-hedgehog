# A fő program, amely meghatározza a játék menetét és a játékos választásai alapján kezeli 
# a logikát.

from .detective_user import *
from .detective_state import *
from .detective_logic import * 

def detective_main():
#a játék fő funkciói.
    reset_score()  # A játék állapotát alaphelyzetbe állítjuk

    role = welcome() # Köszönti a játékost, és bekéri a szerepet (nyomozó vagy gyilkos).
    if not role:
        return # Kilépés, ha a szerepet nem választották ki.

    if role == "detective":
        detective_story() # A nyomozó történetet indítja el.
    elif role == "killer":
        killer_story() # A gyilkos történetet indítja el.

    print("\nA játék véget ért. Az elért pontszámod: 90 /", get_score()) # A szerzett  pontok alapján a játék végének értékelése és a játékos pontszámának kiírása.
    if role == "detective":
        if get_score() == 90 or get_score() == 85 or get_score() == 80:
            print("Gratulálok a sikeres nyomozáshoz! Megtaláltad a gyilkost és az informátort és fényt derítettél az öt évvel ezelőtti bűntényre.")
        elif get_score() >= 70:
            print("Jól játszottál, de nem találtad meg az informátort. Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnáljuk, nem sikerült elkapnod a gyilkost.")
    elif role == "killer":
        if get_score() >= 65 and get_score() <= 90:
            print("Gratulálok! Megúsztad a lebukást! A játék véget ért.")
        elif get_score() >= 115:
            print("Gratulálok! Lebuktál! Azzal, hogy megmentetted a professzort, felfedted magad, így elkaptak! Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnos lebuktál! A játék véget ért.")

    new_play = retry_exit() # Újrajátszás esetén megadja a választási lehetőségeket a felhasználónak - a user felületről meghívva
    if not new_play:
        return

    reset_score()  # Újraindítja a pontszámot

    if new_play == "detective":
        detective_story()
    elif new_play == "killer":
        killer_story()

    print("\nA játék véget ért. Az elért pontszámod: 90 /", get_score())
    if new_play == "detective":
        if get_score() == 90 or get_score() == 85 or get_score() == 80:
            print("Gratulálok a sikeres nyomozáshoz! Megtaláltad a gyilkost és az informátort és fényt derítettél az öt évvel ezelőtti bűntényre.")
        elif get_score() >= 70:
            print("Jól játszottál, de nem találtad meg az informátort. Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnáljuk, nem sikerült elkapnod a gyilkost.")
    elif new_play == "killer":
        if get_score() >= 65 and get_score() <= 90:
            print("Gratulálok! Megúsztad a lebukást! A játék véget ért.")
        elif get_score() >= 115:
            print("Gratulálok! Lebuktál! Azzal, hogy megmentetted a professzort, felfedted magad, így elkaptak! Sok szerencsét legközelebb. A játék véget ért.")
        else:
            print("Sajnos lebuktál! A játék véget ért.")
