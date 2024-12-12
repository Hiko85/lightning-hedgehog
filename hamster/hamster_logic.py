def hamster_welcome():
    input("Üdv a hörcsög tamagotchi játékban! \nA feladatod, hogy gondokodj egy hörcsögről. Nyomj egy ENTERt, ha kezdhetjük!")
    print("Start")

def hamster_name():
    horcsog_nev = input("Először is nevezd el a hörcsögöt: ")
    horcsog_fajta = input(f"Milyen fajta hörcsög {horcsog_nev}? \nAdd meg a hörcsögfajtához tatozó számot: \n1 - Törpe Roborovski \n2 - Campbell törpe orosz \n3 - Szíriai (arany) hörcsög\n")