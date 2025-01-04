import random

# Üdvözlés
def hamster_welcome():
    input("Üdv a hörcsög tamagotchi játékban! \nA feladatod, hogy gondoskodj egy hörcsögről. Nyomj egy ENTERt, ha kezdhetjük! ")
    print("Start")

# Elnevezés
hamster_name = ""  # globális változó
health_meter = 7  # Kezdeti egészségi állapot

def hamster_name_input():
    global hamster_name
    hamster_name = input("Először is nevezd el a hörcsögöt: ")
    print(f"{hamster_name} most már a hörcsögöd!")

# Véletlenszerű szükséglet választása az egészségi állapot alapján
def hamster_needs():
    global health_meter
    print(f"\n{hamster_name} egészségi állapota: {health_meter}/10")

    # Az egészségi állapot alapján válasszon véletlenszerű igényt
    if health_meter >= 7:
        needs = random.choice(["etetés", "ivás", "játék", "alvás"])
    elif health_meter >= 4:
        needs = random.choice(["etetés", "ivás", "alvás"])
    else:
        needs = random.choice(["ivás", "alvás"])

    print(f"\n{hamster_name} most szeretne {needs}-t!")

    if needs == "etetés":
        hamster_food()
    elif needs == "ivás":
        hamster_drink()
    elif needs == "játék":
        hamster_play()
    elif needs == "alvás":
        hamster_sleep()

# Etetés
def hamster_food():
    global hamster_name, health_meter
    print(f"\n{hamster_name}, a hörcsögöd éhes! Mit adsz neki enni?")
    print("A) Zöldségeket")
    print("B) Csipszet")

    hamster_fullness = 5  # Kezdje közepes jóllakottsággal
    cal_counter = 0

    while hamster_fullness < 10:
        answer = input("Válassz, A vagy B: ")
        
        if answer.lower() == "a":
            print(f"{hamster_name} nagyon örül a friss zöldségeknek! Jól választottál.")
            hamster_fullness += 2
            cal_counter += 2
            health_meter += 2  # Az egészségi állapot javul
            print(f"{hamster_name} eddig ennyi kalóriát fogyasztott: {cal_counter}\nJóllakottsága tízes skálán: {hamster_fullness}/10\nEgészségi állapota tízes skálán: {health_meter}/10")
            
        elif answer.lower() == "b":
            print(f"{hamster_name} nem igazán szereti a csipszet, de nem bánja annyira.")
            hamster_fullness += 5
            cal_counter += 10
            health_meter -= 2  # Az egészségi állapot csökken
            print(f"{hamster_name} eddig ennyi kalóriát fogyasztott: {cal_counter}\nJóllakottsága tízes skálán: {hamster_fullness}/10\nEgészségi állapota tízes skálán: {health_meter}/10")

        else:
            print("Érvénytelen válasz, próbáld újra!")

        while hamster_fullness < 10 and answer.lower() not in ["a", "b"]:
            print("Kérlek, válassz A vagy B közül!")
            answer = input("Válassz, A vagy B: ")
        
        if hamster_fullness >= 10:
            print(f"\n{hamster_name} jóllakott, köszöni szépen!")
            print(f"{hamster_name} összesen ennyi kalóriát fogyasztott: {cal_counter}\nEgészségi állapota tízes skálán: {health_meter}/10")
            break

# Itatás
def hamster_drink():
    global hamster_name, health_meter
    print(f"\n{hamster_name}, a hörcsögöd szomjas! Mit adsz neki inni?")
    print("A) Víz")
    print("B) Üdítő")
    print("C) Tea")

    hamster_thirst = 7  # Kezdetben közepes szomjúsággal
    hydration_level = 5  # Kezdje közepes hidratáltsággal

    while hydration_level < 10:
        answer = input("Válaszd A, B vagy C: ")

        if answer.lower() == "a":
            print(f"{hamster_name} nagyon örül a friss víznek! Jól választottál.")
            hamster_thirst -= 2  # Víz csökkenti a szomjúságot
            hydration_level += 3  # Víz növeli a hidratáltságot
            health_meter += 2  # Az egészségi állapot javul
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}/10\nSzomjúsága tízes skálán: {hamster_thirst}/10\nEgészségi állapota tízes skálán: {health_meter}/10")

        elif answer.lower() == "b":
            print(f"{hamster_name} szívesen iszik egy kis üdítőt, de nem túl hidratáló!")
            hamster_thirst -= 1  # Üdítő csökkenti a szomjúságot
            hydration_level += 1  # Üdítő nem segít sokat a hidratáltságon
            health_meter -= 1  # Az üdítő rontja az egészségi állapotot
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}/10\nSzomjúsága tízes skálán: {hamster_thirst}/10\nEgészségi állapota tízes skálán: {health_meter}/10")

        elif answer.lower() == "c":
            print(f"{hamster_name} szívesen iszik teát, de az sem a legjobb választás!")
            hamster_thirst -= 2  # Tea csökkenti a szomjúságot
            hydration_level += 2  # Tea is segít, de nem annyira, mint a víz
            health_meter -= 1  # Tea is rontja az egészségi állapotot
            print(f"{hamster_name} eddigi hidratáltsági szintje: {hydration_level}/10\nSzomjúsága tízes skálán: {hamster_thirst}/10\nEgészségi állapota tízes skálán: {health_meter}/10")

        else:
            print("Érvénytelen válasz, próbáld újra!")
            
        if hydration_level >= 10:
            print(f"\n{hamster_name} már jól hidratált, köszöni szépen!")
            print(f"{hamster_name} összes hidratáltsága: {hydration_level}/10\nEgészségi állapota tízes skálán: {health_meter}/10")
            break

# Játék
def hamster_play():
    global hamster_name, health_meter
    print(f"\n{hamster_name} szeretne játszani! Mit teszel?")
    print("A) Engedem, hogy a labdáján guruljon.")
    print("B) Tedd vissza a kalitkába pihenni.")
    
    hamster_mood = 5  # Kezdjük közepes hangulattal (1-10 skálán)

    while True:
        valasz = input("Válaszd A vagy B: ")

        if valasz.lower() == "a":
            hamster_mood += 2  # Ha játszik, a hangulat növekszik
            health_meter += 1  # A játék javítja az egészségi állapotot
            print(f"{hamster_name} imádja a játékot és nagyon boldog! Hangulata most: {hamster_mood}/10\nEgészségi állapota tízes skálán: {health_meter}/10")
            break

        elif valasz.lower() == "b":
            hamster_mood -= 1  # Ha pihenni megy, a hangulat csökken
            health_meter -= 1  # A pihenés csökkenti az egészségi állapotot
            print(f"{hamster_name} visszament pihenni, de egy kicsit szomorú. Hangulata most: {hamster_mood}/10\nEgészségi állapota tízes skálán: {health_meter}/10")
            break

        else:
            print("Érvénytelen választás, próbáld újra!")

# Fáradtság kezelése
def hamster_sleep():
    global hamster_name, health_meter
    print(f"\n{hamster_name} pihenni szeretne.")
    print(f"Adj neki időt, hogy pihenjen és feltöltődjön!")
    
    hamster_energy = 5  # Kezdjük közepes energiaszinttel

    while hamster_energy < 10:
        print(f"{hamster_name} energiaszintje: {hamster_energy}/10")
        valasz = input("Szeretnéd, hogy folytassa a pihenést? (Igen/Nem): ")

        if valasz.lower() in ["igen", "i"]:  # Elfogadja az "igen" és "i" válaszokat
            hamster_energy += 2  # Minden pihenéssel nő az energiaszint
            health_meter += 1  # Pihenés javítja az egészségi állapotot
            print(f"{hamster_name} pihen, és energiaszintje most: {hamster_energy}/10\nEgészségi állapota tízes skálán: {health_meter}/10")
        
        elif valasz.lower() in ["nem", "n"]:  # Elfogadja a "nem" és "n" válaszokat
            print(f"{hamster_name} úgy döntött, hogy befejezi a pihenést.")
            break

        else:
            print("Érvénytelen választás, próbáld újra!")

    if hamster_energy >= 10:
        print(f"{hamster_name} most már tele van energiával! Készen áll a következő kihívásra!")
