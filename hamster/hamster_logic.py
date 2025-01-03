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
    health_meter = 10  # Kezdje viszonylag jó egészségi állapotban

    while hamster_fullness < 10:
        answer = input("Válassz, A vagy B: ")
        
        if answer.lower() == "a":
            print(f"{hamster_name} nagyon örül a friss zöldségeknek! Jól választottál.")
            hamster_fullness += 2
            cal_counter += 2
            health_meter += 4
            print(f"{hamster_name} eddig ennyi kalóriát fogyasztott: {cal_counter}\nJóllakottsága tizes skálán: {hamster_fullness}\nEgészségi állapota százas skálán: {health_meter}")
            
        elif answer.lower() == "b":
            print(f"{hamster_name} nem igazán szereti a csipszet, de nem bánja annyira.")
            hamster_fullness += 5
            cal_counter += 10
            health_meter -= 3
            print(f"{hamster_name} eddig ennyi kalóriát fogyasztott: {cal_counter}\nJóllakottsága tizes skálán: {hamster_fullness}\nEgészségi állapota százas skálán: {health_meter}")

        else:
            print("Érvénytelen válasz, próbáld újra!")
            continue
        
        # Ha a hörcsög jól lakott, megállunk
        if hamster_fullness >= 10:
            print(f"\n{hamster_name} jóllakott, köszöni szépen!")
            print(f"{hamster_name} összesen ennyi kalóriát fogyasztott: {cal_counter}\nEgészségi állapota százas skálán: {health_meter}")
            break

        # Ha az egészségi állapot túl alacsony, zöldséget adunk neki
        if health_meter < 10:
            print(f"{hamster_name} nincs valami jó formában, adj neki zöldséget!")


# Itatás
def hamster_drink():
    global hamster_name
    print(f"\n{hamster_name}, a hörcsögöd szomjas! Mit adsz neki inni?")
    print("A) Víz")
    print("B) Üdítő")

    hamster_thirst = 0
    hydration_level = 5  # Kezdje viszonylag jó hidratáltsággal
    health_meter = 10  # Kezdje viszonylag jó egészségi állapotban

    while hamster_thirst < 10:
        answer = input("Válassz, A vagy B: ")
        
        if answer.lower() == "a":
            print(f"{hamster_name} nagyon örül a friss víznek! Jól választottál.")
            hamster_thirst += 2
            hydration_level += 3  # Víz növeli a hidratáltságot
            health_meter += 2
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}\nSzomjúsága tizes skálán: {hamster_thirst}\nEgészségi állapota százas skálán: {health_meter}")
            
        elif answer.lower() == "b":
            print(f"{hamster_name} szívesen iszik egy kis üdítőt, de nem túl hidratáló!")
            hamster_thirst += 5
            hydration_level += 1  # Üdítő nem segít sokat a hidratáltságon
            health_meter -= 4
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}\nSzomjúsága tizes skálán: {hamster_thirst}\nEgészségi állapota százas skálán: {health_meter}")

        else:
            print("Érvénytelen válasz, próbáld újra!")
        
        # Ha a hörcsög jól itta, megállunk
        if hamster_thirst >= 10:
            print(f"\n{hamster_name} már jól hidratált, köszöni szépen!")
            print(f"{hamster_name} összes hidratáltsága: {hydration_level}\nEgészségi állapota százas skálán: {health_meter}")
            break

        # Ha az egészségi állapot túl alacsony, vízre van szüksége
        if health_meter < 10:
            print(f"{hamster_name} nincs valami jó formában, adj neki vizet!")


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