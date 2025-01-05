#Nyomonköveti a játék állapotát, a játékos szerzett pontszámait.
# Globális változó a pontszám tárolására
score = 0

def update_score(points):
    # Növeli a pontszámot
    global score
    score += points

def get_score():
    # Visszaadja az aktuális pontszámot
    return score

def reset_score():
    # A pontszám visszaállítása 0-ra
    global score
    score = 0