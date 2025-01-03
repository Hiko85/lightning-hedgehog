# Üdvözlés
def hamster_welcome():
    input("Üdv a hörcsög tamagotchi játékban! \nA feladatod, hogy gondoskodj egy hörcsögről. Nyomj egy ENTERt, ha kezdhetjük! ")
    print("Start")

# Elnevezés
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

#Etetés
def hamster_food():
    global hamster_name
    print(f"\n{hamster_name}, a hörcsögöd éhes! Mit adsz neki enni?")
    print("A) Zöldségeket")
    print("B) Csipszet")

    hamster_fullness = 0
    cal_counter = 0
    health_meter = 0

    while hamster_fullness < 10 :
        answer = input("Válassz, A vagy B: ")
        if answer.lower() == "a":
            print(f"{hamster_name} nagyon örül a friss zöldségeknek! Jól választottál.")
            hamster_fullness += 1
            cal_counter += 2
            health_meter += 4
            print(f"{hamster_name} eddig ennyi kalóriát fogyasztott: {cal_counter}")
            print(f"{hamster_name} egészségi állapotia tízes skálán: {health_meter}")
        elif answer.lower() == "b":
            print(f"{hamster_name} nem igazán szereti a csipszet, de nem bánja annyira.")
            hamster_fullness += 2
            cal_counter += 10
            health_meter -= 3
            print(f"{hamster_name} eddig ennyi kalóriát fogyasztott: {cal_counter}")
            print(f"{hamster_name} egészségi állapotia tízes skálán: {health_meter}")
        else:
            print("Érvénytelen válasz, próbáld újra!")

    if hamster_fullness == 10 :
            print(f"{hamster_name} jól lakott, köszöni szépen!")

# Itatás
# def hamster_food():
    # global hamster_name
    # print(f"\n{hamster_name}, a hörcsögöd éhes! Mit adsz neki enni?")
    # print("A) Zöldségeket")
    # print("B) Csipszet")

    # hamster_fullness = 0

    # while hamster_fullness < 10 :
    #     answer = input("Válassz, A vagy B: ")
    #     if answer.lower() == "a":
    #         print(f"{hamster_name} nagyon örül a friss zöldségeknek! Jól választottál.")
    #         hamster_fullness += 1
    #         print(hamster_fullness)
    #     elif answer.lower() == "b":
    #         print(f"{hamster_name} nem igazán szereti a csipszet, de nem bánja annyira.")
    #         hamster_fullness -= 1
    #         print(hamster_fullness)
    #     else:
    #         print("Érvénytelen válasz, próbáld újra!")

    # if hamster_fullness == 10 :
    #         print(f"{hamster_name} jól lakott, köszöni szépen!")

# # Játék
#     print("\nMost a hörcsögöd szeretne játszani. Mit teszel?")
#     print("A) Engedem, hogy a labdáján guruljon.")
#     print("B) Tedd vissza a kalitkába pihenni.")
#     valasz = input("Válaszd A vagy B: ")

#     if valasz.lower() == "a":
#         print("A hörcsögöd imádja a játékot és nagyon boldog!")
#     elif valasz.lower() == "b":
#         print("A hörcsögöd pihenhet, de egy kicsit unatkozik.")
#     else:
#         print("Érvénytelen válasz, próbáld újra!")
#         return

# # Alvás
#     print("\nA hörcsögöd fáradt. Mit csinálsz?")
#     print("A) Tedd a fészkébe, hogy pihenhessen.")
#     print("B) Hadd maradjon kint egy kicsit.")
#     valasz = input("Válaszd A vagy B: ")

#     if valasz.lower() == "a":
#         print("A hörcsögöd kipiheni magát, és boldog, hogy kényelmesen alhatott.")
#     elif valasz.lower() == "b":
#         print("A hörcsögöd nem tud aludni, és kicsit fáradtabb lesz.")
#     else:
#         print("Érvénytelen válasz, próbáld újra!")
#         return

#     # Játék vége
#     print("\nA játék véget ért! Gratulálok, sikeresen gondoskodtál a hörcsögödről!")
#     print("Köszönöm, hogy játszottál!")

# # Játék elindítása
# # jatek()