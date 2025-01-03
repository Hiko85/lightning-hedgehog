def hamster_welcome():
    input("Üdv a hörcsög tamagotchi játékban! \nA feladatod, hogy gondoskodj egy hörcsögről. Nyomj egy ENTERt, ha kezdhetjük! ")
    print("Start")

hamster_name = "" # globális változó

def hamster_name():
    global hamster_name
    hamster_name = input("Először is nevezd el a hörcsögöt: ")
    hamster_type = int(input(f"Milyen fajta hörcsög {hamster_name}? \nAdd meg a hörcsögfajtához tatozó számot: \n1 - Törpe Roborovski \n2 - Campbell törpe orosz \n3 - Szíriai (arany) hörcsög\n"))
    
    if hamster_type == 1 :
        print(f"{hamster_name} egy csodálatos Törpe Roborovski!")
    elif hamster_type == 2 :
        print(f"{hamster_name} egy utánozhatatlan Campbell törpe orosz!")
    elif hamster_type == 3 :
        print(f"{hamster_name} egy felejthetetlen Szíriai (arany) hörcsög!")

def hamster_food():
    global hamster_name
    print(f"\n{hamster_name}, a hörcsögöd éhes! Mit adsz neki enni?")
    print("A) Zöldségeket")
    print("B) Csipszet")

    hamster_fullness = 0

    while hamster_fullness < 10 :
        answer = input("Válassz, A vagy B: ")
        if hamster_fullness == 10 :
            print(f"{hamster_name} jól lakott, köszöni szépen!")
        elif answer.lower() == "a":
            print(f"{hamster_name} nagyon örül a friss zöldségeknek! Jól választottál.")
            hamster_fullness += 1
            print(hamster_fullness)
        elif answer.lower() == "b":
            print(f"{hamster_name} nem igazán szereti a csipszet, de nem bánja annyira.")
            hamster_fullness -= 1
            print(hamster_fullness)
        else:
            print("Érvénytelen válasz, próbáld újra!")


