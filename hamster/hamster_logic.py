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

        while hamster_fullness < 10 and answer.lower() not in ["a", "b"]:
            print("Kérlek, válassz A vagy B közül!")
            answer = input("Válassz, A vagy B: ")
        
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
    print("C) Tea")

    hamster_thirst = 10  # Kezdetben szomjas a hörcsög
    hydration_level = 5  # Kezdje viszonylag jó hidratáltsággal
    health_meter = 10  # Kezdje viszonylag jó egészségi állapotban

    while hamster_thirst > 0:  # Amíg nem lesz teljesen hidratált
        answer = input("Válaszd A, B vagy C: ")

        if answer.lower() == "a":
            print(f"{hamster_name} nagyon örül a friss víznek! Jól választottál.")
            hamster_thirst -= 5  # Víz csökkenti a szomjúságot
            hydration_level += 3  # Víz növeli a hidratáltságot
            health_meter += 2
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}\nSzomjúsága tizes skálán: {hamster_thirst}\nEgészségi állapota százas skálán: {health_meter}")

        elif answer.lower() == "b":
            print(f"{hamster_name} szívesen iszik egy kis üdítőt, de nem túl hidratáló!")
            hamster_thirst -= 2  # Üdítő csökkenti a szomjúságot
            hydration_level += 1  # Üdítő nem segít sokat a hidratáltságon
            health_meter -= 4  # Az üdítő rontja az egészségi állapotot
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}\nSzomjúsága tizes skálán: {hamster_thirst}\nEgészségi állapota százas skálán: {health_meter}")

        elif answer.lower() == "c":
            print(f"{hamster_name} szívesen iszik teát, de az sem a legjobb választás!")
            hamster_thirst -= 3  # Tea csökkenti a szomjúságot
            hydration_level += 2  # Tea is segít, de nem annyira, mint a víz
            health_meter -= 2  # Tea is rontja az egészségi állapotot
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}\nSzomjúsága tizes skálán: {hamster_thirst}\nEgészségi állapota százas skálán: {health_meter}")

        else:
            print("Érvénytelen válasz, próbáld újra!")
            
        # Ha a hörcsög jól hidratált, megállunk
        if hamster_thirst <= 0:
            print(f"\n{hamster_name} már jól hidratált, köszöni szépen!")
            print(f"{hamster_name} összes hidratáltsága: {hydration_level}\nEgészségi állapota százas skálán: {health_meter}")
            break  # Kilépünk a ciklusból, ha a hörcsög már hidratált

        # Ha az egészségi állapot túl alacsony, vízre van szüksége
        if health_meter < 5:  # Ha az egészségi állapot túl alacsony, vizet kell adni
            print(f"{hamster_name} nincs valami jó formában, adj neki vizet!")


# Játék
def hamster_play():
    global hamster_name
    print(f"\n{hamster_name} szeretne játszani! Mit teszel?")
    print("A) Engedem, hogy a labdáján guruljon.")
    print("B) Tedd vissza a kalitkába pihenni.")
    
    hamster_mood = 5  # Kezdjük közepes hangulattal (1-10 skálán)

    while True:  # Ciklus, hogy csak érvényes válasz után lépjen tovább
        valasz = input("Válaszd A vagy B: ")

        if valasz.lower() == "a":
            hamster_mood += 2  # Ha játszik, a hangulat növekszik
            print(f"{hamster_name} imádja a játékot és nagyon boldog! Hangulata most: {hamster_mood}/10")
            break  # Ha válaszolt, kilépünk a ciklusból

        elif valasz.lower() == "b":
            hamster_mood -= 1  # Ha pihen, a hangulat kissé csökken
            print(f"{hamster_name} pihenhet, de egy kicsit unatkozik. Hangulata most: {hamster_mood}/10")
            break  # Ha válaszolt, kilépünk a ciklusból

        else:
            print("Érvénytelen válasz, próbáld újra!")  # Ha érvénytelen választ adunk, újra kérdez

    # A hangulat értéke alapján különböző reakciók:
    if hamster_mood >= 8:
        print(f"{hamster_name} most igazán boldog és energikus!")
    elif hamster_mood >= 5:
        print(f"{hamster_name} elég jól van, de egy kis mókára vágyik.")

        # Ha a hörcsög jól van, folytathatjuk a játékot
        print(f"\nMiután {hamster_name} jól van, most még egy újabb lehetőséget adunk neki!")

        # Új lehetőség, ha a hörcsög továbbra is jól van
        print("A) Vidd el sétálni a parkba.")
        print("B) Adj neki egy kis finomságot.")
        
        while True:
            valasz = input("Válaszd A vagy B: ")

            if valasz.lower() == "a":
                print(f"{hamster_name} nagyon élvezi a parkban tett sétát!")
                break  # Kilépünk a ciklusból, ha válaszolt

            elif valasz.lower() == "b":
                print(f"{hamster_name} imádja a finomságokat, boldog lesz tőle!")
                break  # Kilépünk a ciklusból, ha válaszolt

            else:
                print("Érvénytelen válasz, próbáld újra!")  # Ha érvénytelen választ adunk, újra kérdez

    else:
        print(f"{hamster_name} kicsit lehangolt, talán egy kis játék segíthet neki.")



# Pihenés
def hamster_rest():
    global hamster_name
    print(f"\n{hamster_name} fáradt. Mit csinálsz?")
    print("A) Tedd a fészkébe, hogy pihenhessen.")
    print("B) Hadd maradjon kint egy kicsit.")

    hamster_mood = 6  # Kezdjük egy közepes hangulattal
    hamster_tiredness = 8  # Kezdjük egy magas fáradtság szinttel

    while True:  # Ciklus, hogy csak érvényes válasz után lépjen tovább
        valasz = input("Válaszd A vagy B: ")

        if valasz.lower() == "a":
            hamster_tiredness -= 3  # Pihenés csökkenti a fáradtságot
            hamster_mood += 1  # Pihenés növeli a hangulatot
            print(f"{hamster_name} kipiheni magát, és boldog, hogy kényelmesen alhatott.")
            print(f"Hangulata: {hamster_mood}/10, Fáradtsága: {hamster_tiredness}/10")
            break  # Ha válaszolt, kilépünk a ciklusból

        elif valasz.lower() == "b":
            hamster_tiredness += 2  # Ha nem pihen, a fáradtság nő
            hamster_mood -= 1  # A fáradtság csökkenti a hangulatot
            print(f"{hamster_name} nem tud aludni, és kicsit fáradtabb lesz.")
            print(f"Hangulata: {hamster_mood}/10, Fáradtsága: {hamster_tiredness}/10")
            break  # Ha válaszolt, kilépünk a ciklusból

        else:
            print("Érvénytelen válasz, próbáld újra!")  # Ha érvénytelen választ adunk, újra kérdez

    # A hangulat és fáradtság értéke alapján különböző reakciók:
    if hamster_tiredness <= 3:
        print(f"{hamster_name} most már kipihent és energikus!")
    elif hamster_mood >= 5:
        print(f"{hamster_name} pihenhetett, de még mindig jól van!")
    else:
        print(f"{hamster_name} nagyon fáradt, szüksége van egy hosszabb pihenésre.")

    # Játék vége vagy folytatás
    if hamster_mood >= 6:
        print("\nA játék folytatódik, mivel a hörcsögöd jól van!")
    else:
        print("\nA játék véget ért! A hörcsögöd túl fáradt volt, hogy folytassa.")
    print("Köszönöm, hogy játszottál!")
