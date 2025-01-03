def hamster_welcome():
    input("Üdv a hörcsög tamagotchi játékban! \nA feladatod, hogy gondokodj egy hörcsögről. Nyomj egy ENTERt, ha kezdhetjük!")
    print("Start")

def hamster_name():
    hamster_name = input("Először is nevezd el a hörcsögöt: ")
    hamster_type = int(input(f"Milyen fajta hörcsög {hamster_name}? \nAdd meg a hörcsögfajtához tatozó számot: \n1 - Törpe Roborovski \n2 - Campbell törpe orosz \n3 - Szíriai (arany) hörcsög\n"))
    
    if hamster_type == 1 :
        print(f"{hamster_name} egy csodálatos Törpe Roborovski!")
    elif hamster_type == 2 :
        print(f"{hamster_name} egy utánozhatatlan Campbell törpe orosz!")
    elif hamster_type == 3 :
        print(f"{hamster_name} egy felejthetetlen Szíriai (arany) hörcsög!")

def hamster_food():
    print("\nA hörcsögöd éhes! Mit adsz neki enni?")
    print("A) Zöldségeket")
    print("B) Csipszet")
    answer = input("Válaszd A vagy B: ")

    if answer.lower() == "a":
        print("A hörcsögöd nagyon örül a friss zöldségeknek! Jól választottál.")
    elif answer.lower() == "b":
        print("A hörcsögöd nem igazán szereti a csipszet, de nem bánja annyira.")
    else:
        print("Érvénytelen válasz, próbáld újra!")