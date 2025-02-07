#főoldal ami kapcsolatba lépjen a felhasználóval
def welcome ():
    print("A nyomozós játékot választottad!")
    print("\nAz alaptörténet: Öt évvel ezelőtt, október 1-én az elsőéves Kamonohashi Ront választották ki egy gyakorlatra, hogy a rendőrséggel együtt dolgozzon egy hét bérgyilkosból álló csoport elfogásán. Ron megfejtette a bűnözők által használt kódot, és megtalálta a rejtekhelyüket egy elszigetelt gyárban. Délután négykor egyedül indult oda. Amikor a rendőrség egy órával később megérkezett, Ront a gyilkosok holttestei között találták, sérülésekkel borítva és egy késsel a kezében. Ron nem emlékszik az eseményekre, és az eset rejtély maradt.")

    choice = "" # A felhasználói választ tároló változó.

    while choice != "3":
        print("\nVálaszd ki, ki szeretnél lenni?")
        print("1. Nyomozó")
        print("2. Gyilkos")
        print("3. Kilépés")
        choice = input("Válassz egyet 1-3-ig: ").strip()

        if choice == "1":
            print("\nA nyomozó szerepet választottad...\n")
            return "detective"
        elif choice == "2":
            print("\nA gyilkos szerepet választottad...\n")
            return "killer"
        elif choice == "3":
            print("\nKöszönjük, hogy játszottál! Viszlát!\n")
            return None
        else:
            print("Érvénytelen választás. Kérlek, próbáld újra.")
            return welcome()

#lehetőség az újrakezdésre vagy a kilépésre a játék végén.
def retry_exit():

    choice = ""

    while choice != "3":
        print("\nMit szeretnél tenni?")
        print("1. Újrajátszani a játékot nyomozóként.")
        print("2. Újrajátszani a játékot gyilkosként.")
        print("3. Kilépni.")
        choice = input("Választásod: ").strip()

        if choice == "1":
            print("\nNyomozóként újrakezded a játékot...\n")
            return "detective"
        elif choice == "2":
            print("\nA gyilkos szerepet választottad...\n")
            return "killer"
        elif choice == "3":
            print("\nKöszönjük, hogy játszottál! Viszlát!\n")
            return None
        else:
            print("Érvénytelen választás. Kérlek, próbáld újra.")
            return retry_exit()
