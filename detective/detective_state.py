class GameState:
#Nyomonköveti a játék állapotát, a játékos szerzett pontszámait.
    def __init__(self):
        self.score = 0

    def update_score(self, points):
#Frissíti a játékos pontszámait, a megadott pontszámokat alapján.
        self.score += points

    def get_score(self):
#Kiírja a kapott pontszámot.
        return self.score
    def reset(self):
        self.score = 0