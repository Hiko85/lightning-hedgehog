def welcome ():
    print("A nyomozós játékot választottad!")
    print("Az alaptörténet: Öt évvel ezelőtt, október 1-én az elsőéves Kamonohashi Ront választották ki egy gyakorlatra, hogy a rendőrséggel együtt dolgozzon egy hét bérgyilkosból álló csoport elfogásán. Ron megfejtette a bűnözők által használt kódot, és megtalálta a rejtekhelyüket egy elszigetelt gyárban. Délután négykor egyedül indult oda. Amikor a rendőrség egy órával később megérkezett, Ront a gyilkosok holttestei között találták, sérülésekkel borítva és egy késsel a kezében. Ron nem emlékszik az eseményekre, és az eset rejtély maradt.")

    choice = ""

    while choice != "":
        print("\nVálaszd ki, ki szeretnél lenni?")
        print("1. Nyomozó")
        print("2. Gyilkos")
        print("3. Kilépés")
        choice = input("Válassz egyet 1-3-ig").strip()

        if choice == "1":
            print("\nA nyomozó szerepet választottad...\n")
        elif choice == "2":
            print("\nA gyilkos szerepet választottad...\n")
        elif choice == "3":
            print("\nKöszönjük, hogy játszottál! Viszlát!\n")
        else:
            print("Érvénytelen választás. Kérlek, próbáld újra.")
