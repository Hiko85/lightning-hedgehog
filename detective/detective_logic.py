def detective_story(state):
#A nyomozó történetet kezeli.
    
    print("Öt év telt el azóta, hogy Ront meggyanúsították a gyilkossággal és kicsapták a nyomozó akadémiáról. Nyomozóként korábban már többször kérted Ron segítségét," 
          "aki így titokban mégis nyomozhat, ám most Ron meghívót kapott Milo Moriarty-tól egy hajóútra. Felfedi, hogy az akadémia tanárai közül is részt vesznek az úton"
          " páran, köztük az is, aki annak idején besározta Ront. Mit tesztek?")
    print("1. Elfogadjátok a meghívást és elmentek a hajóútra.")
    print("2. Nem érdekelnek a Moriarty-k, otthon maradtok.")

    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nA hajón összefutottok négy ismerőssel: a zártszobás gyilkosságok szakértőjével (Fin tanárnő), egy orvossal (Dr. Hirsch), illetve Ron két volt diáktársával"
              " (Shachival és Elmerrel). Mindegyikük gyanús indokkal van a hajón, ám újabb üzenetet kaptok Milótól, miszerint aznap este éjfélkor a bárban olyan információhoz"
              " juthattak, ami az igazi gyilkos nyomára vezethet. Elmentek a bárba, ahol az egyik vendég éjfélkor hirtelen életét veszti. Dr. Hirsch, aki szintén az akadémia"
               " tanára, ugyancsak a bárban van, és megtiltja, hogy bárki is elhagyja a bárt. Mit tesztek?")
        print("1. Megvizsgáljátok a holttestet.")
        print("2. Kikérdezitek a jelenlévőket.\n")
        print("Jelenlegi pontszámod:", state.get_score())
        return bar_murder(state)
    elif choice == "2":
        state.update_score(0)
        print("\nA választásod alapján sosem tudjátok meg ki az igazi gyilkos. A nyomozás sikertelen volt. Elbuktál.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)


def retry_or_exit(state):
    print("1. Újrapróbálod a játékot nyomozóként?")
    print("2. Kipróbálod a gyilkos történetét?")
    print("3. Kilépés a játékból.")
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.reset()  # Reset score
        detective_story(state)
    elif choice == "2":
        state.reset()  # Reset score
        killer_story(state)
    elif choice == "3":
        print("Köszönjük, hogy játszottál! Viszlát!")
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        retry_or_exit(state)

def bar_murder(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(5)
        print("\nAz orvos egyszerűen közli, hogy méreg végzett az áldozattal. Ráadásul a bort az áldozat feleségének kérésére hozták, ám a pincér szerint egy férfi hang"
              " adta le korábban a rendelést. Eközben Milo felhívja Ront, akitől megtudjátok, hogy a gyilkosságot az követte el, aki után Ron is nyomoz, vagyis "
              "a Moriarty család informátora, és ahhoz, hogy megállítsák, Ronnak meg kell ölnie. Hogyan tovább?")
        print("\n1. Megtagadjátok Milo parancsát, nem akarjátok megölni az informátort.")
        print("2. Tovább nyomoztok, hogy megtudjátok, ki az informátor.")
        print("Jelenlegi pontszámod:", state.get_score())
        return questioning_examining(state)
    elif choice == "2":
        state.update_score(10)
        print("\nAz orvos egyszerűen közli, hogy méreg végzett az áldozattal. Ráadásul a bort az áldozat feleségének kérésére hozták, ám a pincér szerint egy férfi hang"
              " adta le korábban a rendelést. Eközben Milo felhívja Ront, akitől megtudjátok, hogy a gyilkosságot az követte el, aki után Ron is nyomoz, vagyis "
              "a Moriarty család informátora, és ahhoz, hogy megállítsák, Ronnak meg kell ölnie. Hogyan tovább?")
        print("\n1. Megtagadjátok Milo parancsát, nem akarjátok megölni az informátort.")
        print("2. Tovább nyomoztok, hogy megtudjátok, ki az informátor.")
        print("Jelenlegi pontszámod:", state.get_score())
        return questioning_examining(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)    

def questioning_examining(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(0)
        print("\nMegtagadtátok Milo parancsát, a gyilkosságok tovább folytatódnak. Nem kaptátok el a gyilkost. Vesztettetek. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    elif choice == "2":
        state.update_score(10)
        print("\nAz ebédlőben összefutottatok Fin tanárnőnel és Shachival, az asszisztensével. Ron a tanárnőt kérdezi az öt évvel ezelőtti gyilkosságról."
              " Te pedig arról, hogy aznap mikor látta utoljára Ront. A tanárnő elmondása alapján Ron a megszokottól eltérően viselkedett és közvetlenül a találkozójuk "
              "után történt a gyilkosság. Shachi meggyőződése, hogy Ron tette, ám mielőtt belemerülhetnétek a részletekbe sikítást hallotok és kimentek a hajótatra. "
              "Nem láttok semmit, majd hirtelen lezuhan valaki. Mit tesztek?")
        print("1. Megvizsgáljátok a testet.")
        print("2. Felmentek, hogy megnézzétek a helyszínt, ahonnan az áldozat lezuhant.")
        print("Jelenlegi pontszámod:", state.get_score())
        return continue_investigation(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)

def continue_investigation(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(5)
        print("\nA felső szinten egy lányt találtok halálra rémülve, aki elmondja, hogy amikor magához tért meg volt kötözve, ezért elvágta a köteleket. "
              "Ron ebből rögtön rájön, hogy a gyilkos úgy intézte a gyilkosságot, hogy neki ne kelljen ott lennie. Míg az egyik lány a fedélzeten feküdt megkötözve, "
              "addig a másikat hozzákötözte és lelógatta a tatról. Amikor felébredt és elvágta a köteleket ezzel a lelógó társát már nem tartotta meg semmi. Mit tesztek ezután?")
        print("1. Tovább nyomoztok az informátor után.")
        print("2. Feladjátok.")
        print("Jelenlegi pontszámod:", state.get_score())
        return falling_body(state)
    elif choice == "2":
        state.update_score(10)
        print("\nA felső szinten egy lányt találtok halálra rémülve, aki elmondja, hogy amikor magához tért meg volt kötözve, ezért elvágta a köteleket. "
              "Ron ebből rögtön rájön, hogy a gyilkos úgy intézte a gyilkosságot, hogy neki ne kelljen ott lennie. Míg az egyik lány a fedélzeten feküdt megkötözve, "
              "addig a másikat hozzákötözte és lelógatta a tatról. Amikor felébredt és elvágta a köteleket ezzel a lelógó társát már nem tartotta meg semmi. Mit tesztek ezután?")
        print("1. Tovább nyomoztok az informátor után.")
        print("2. Feladjátok.")
        print("Jelenlegi pontszámod:", state.get_score())
        return falling_body(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)
    
def falling_body(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nAhhoz, hogy ne történhessen újabb gyilkosság, egy napon belül meg kell találnotok az informátort. Úgy döntötök, hogy elmondjátok a négy gyanúsítottnak, "
              "hogy a Moriarty-család áll a gyilkosságok mögött és, hogy egyikük nekik dolgozik, ezért mind gyanúsak, de segítsenek nektek a nyomozásban. "
              "Ezzel próbáljátok megnehezíteni az informátor dolgát. Úgy döntötök, hogy mind a hatan a hatodik emeleti bárba mentek, mert annak csak egy bejárata van, "
              "így senki nem tud észrevétlenül meglépni. Ám míg várakoztok, a doktor egy üzenetet talál, ami a harmadik gyilkosságra utal: éjfél után 10 perccel "
              "a .01-es szobában történik. Mit tesztek?")
        print("1. Mivel hatan vagytok és hat emeleten található 01-es szoba, mindenki elmegy egy emeletre és figyelmezteti az ott lakót.")
        print("2. Ellenzitek, hogy szétváljatok.")
        print("Jelenlegi pontszámod:", state.get_score())
        return investigating_informator(state)
    elif choice == "2":
        state.update_score(0)
        print("\nFeladtátok. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)

def investigating_informator(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nBeosztották, hogy ki melyik szintre megy. Miután megvizsgáltad a 101-es szobát visszamész Ronhoz a hatodikra. Ron elmondja, hogy szerinte nem "
              "valamelyik szobára utal a hátrahagyott nyom, és csak azért ment bele abba, hogy szétváljanak, hogy megnézze, ki, mit csinál és hogy míg odavannak, "
              "megfejtse a kód igazi jelentését. Miután rákérdeztél, hogy sikerült-e rájönnie azt felelte, hogy rád várt, hátha te észrevettél valamit. Mit felelsz?")
        print("1. Nem vettél észre semmi különöset, azon kívül, hogy furcsállod miért csak hat emeleten vannak szobák, amikor a hajó hétemeletes.")
        print("2. Nincs ötleted.")
        print("Jelenlegi pontszámod:", state.get_score())
        return separate(state)
    elif choice == "2":
        state.update_score(10)
        print("\nHosszas huzavona után, Ron mégis úgy dönt, hogy belemegy abba, miszerint emeletenként 1-1 ember beszéljen a .01-es szobák lakóival. "
              "Miután megvizsgáltad a 101-es szobát visszamész Ronhoz a hatodikra. Ron elmondja, hogy szerinte nem valamelyik szobára utal a hátrahagyott nyom, "
              "és csak azért ment bele abba, hogy szétváljanak, hogy megnézze, ki, mit csinál és hogy míg odavannak, megfejtse a kód igazi jelentését. "
              "Miután rákérdeztél, hogy sikerült-e rájönnie azt felelte, hogy rád várt, hátha te észrevettél valamit. Mit felelsz?")
        print("1. Nem vettél észre semmi különöset, azon kívül, hogy furcsállod miért csak hat emeleten vannak szobák, amikor a hajó hétemeletes.")
        print("2. Nincs ötleted.")
        print("Jelenlegi pontszámod:", state.get_score())
        return oppose(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)

def separate(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nAz észrevételed alapján Ron rájön, hogy nem szobakódra utalt az üzenet, hanem a Pool szó első két betűjét takarták ki, ezért a hetedikre mentek "
              "a medencéhez. Ahogy odaértek két összekötözött férfi esett épp a medencébe, de közben egy árnyat láttok a szoba másik bejáratánál. Mit tesztek?")
        print("1. Te megmented a medencébe esett férfiakat, Ront pedig hagyod, hogy a tettes után menjen.")
        print("2. Mindketten a tettes után szaladtok.")
        print("Jelenlegi pontszámod:", state.get_score())
        return pool(state)
    elif choice == "2":
        state.update_score(0)
        print("\nElbuktatok. Nem jöttetek rá, hogy mit jelentett igazából a kód, újabb áldozatok haltak meg. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)

def oppose(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nAz észrevételed alapján Ron rájön, hogy nem szobakódra utalt az üzenet, hanem a Pool szó első két betűjét takarták ki, ezért a hetedikre mentek "
              "a medencéhez. Ahogy odaértek két összekötözött férfi esett épp a medencébe, de közben egy árnyat láttok a szoba másik bejáratánál. Mit tesztek?")
        print("1. Te megmented a medencébe esett férfiakat, Ront pedig hagyod, hogy a tettes után menjen.")
        print("2. Mindketten a tettes után szaladtok.")
        print("Jelenlegi pontszámod:", state.get_score())
        return pool(state)
    elif choice == "2":
        state.update_score(0)
        print("\nElbuktatok. Nem jöttetek rá, hogy mit jelentett igazából a kód, újabb áldozatok haltak meg. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)

def pool(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nKimentetted a két férfit, közben pedig Ron is visszatér, akinek sajnos nem sikerült elkapnia a tettest. Viszont a tettes elhagyta a műholdas "
              "telefonját, amit így Ron magához vett. Miután a másik négy tag is visszatért a szobák ellenőrzéséből, mindenki elmondja, hogy mit tapasztalt "
              "az egyes szobáknál. Ron elmondja, hogy hamarosan fényt derít a gyilkos kilétére és arra kéri négyüket, hogy maradjanak ott, ahol vannak. "
              "Ti ketten pedig kimentek a helyiségből, hogy telefonáljatok. Az út elején egy segítőtök és volt a hajón, aki pincérnek álcázva magát begyűjtötte"
              " mindenki DNS-ét. Ron arra kérte, hogy vesse össze a mintákat azzal a vérmintával, amit annak idején a gyilkosság helyszínén találtak, "
              "de nem tudták azonosítani. Ennek eredményét kérdezte telefonon a társatoktól, aki elmondja, hogy Elmer DNS volt az. Azonban miután megkaptátok "
              "a választ hirtelen füst jelent meg körülöttetek, amitől mindketten elájultatok. Amikor magatokhoz tértek, egy színházteremben találjátok magatokat, "
              "ahol épp egy bűvészműsor zajlik. A színpadon a bűvész felemeli azt a fegyvert, amit még Milo rejtetett el a szobátokban azért, hogy Ron azzal végezzen "
              "az informátorral. Megakadályozzátok, hogy a bűvész elsüsse az igazi fegyvert és közben észreveszitek, hogy a négy gyanúsított szintén kiütve az első sorban ül. "
              "Megjelenik Milo, aki kíváncsian várja, rájöttetek-e arra, ki a gyilkos és egyben az informátor. Kit választotok?")
        print("1. Dr. Hirsch, az orvos.")
        print("2. Fin tanárnő, aki a zártszobás gyilkosságok szakértője.")
        print("3. Shachi, aki a tanárnő asszisztense és Ron volt diáktársa.")
        print("4. Elmer, aki szintén Ron diáktársa volt és jelenleg nyomozóként dolgozik.")
        print("Jelenlegi pontszámod:", state.get_score())
        return catch_culprit(state)
    elif choice == "2":
        state.update_score(0)
        print("\nElbuktatok. Megmenthettétek volna az áldozatokat, de hagytátok őket meghalni. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(state)

def catch_culprit(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(0)
        print("A végső pontszámod:", state.get_score())
        return
    elif choice == "2":
        state.update_score(0)
        print("A végső pontszámod:", state.get_score())
        return
    elif choice == "3":
        state.update_score(10)
        print("A végső pontszámod:", state.get_score())
        return
    elif choice == "4":
        state.update_score(0)
        print("A végső pontszámod:", state.get_score())
        return
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        detective_story(choice)

def killer_story(state):
    # A gyilkos történetet kezeli.

    print("Öt év telt el azóta, hogy Ront meggyanúsították a gyilkossággal és kicsapták a nyomozó akadémiáról. Te voltál, aki akkor rákented a gyilkosságot, mint a Moriarty-család informátora hiszen az akadémia diákjaként könnyen ráterhelhetted a gyanút."
          "Most az a feladatod, hogy a hajóúton Milo parancsára gyilkosságokat hajts végre, de ne hagyd, hogy Ron és a társa leleplezzenek téged."
          "A hajón már indulás előtt összefutsz Ronnal és a társával. Mit teszel?")
    print("1. Úgy teszel, mintha nem ismernéd őket.")
    print("2. Mivel Fin professzorral vagy együtt, inkább te is szóbaelegyedsz velük.")

    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(0)
        print(
            "\nFin professzor megfed, amiért udvariatlanul viselkedtél. Tiszteled a tanárnőt, így... Mit teszel?")
        print("1. Bocsánatot kérsz Rontól és a társától.")
        print("2. Nem érdekel a két gyökér, inkább elsétálsz.\n")
        print("Jelenlegi pontszámod:", state.get_score())
        return first_meeting(state)
    elif choice == "2":
        state.update_score(10)
        print("\nSzóbaelegyedtek, de nem bírod ki, hogy ne hozd fel az öt évvel ezelőtti gyilkossági ügyet:")
        print("1. Váltig állítod, hogy Ron gyilkos és nem érted, hogy mászkálhat szabadon, így persze vitatkozni kezdtek.")
        print("2. Próbálsz Ron kedvére tenni, így úgy teszel, mintha aki nagyon sajnálja, hogy anno igazságtalanul vádolták meg a gyilkossággal.\n")
        print("Jelenlegi pontszámod:", state.get_score())
        return first_meeting_talk(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)


def retry_or_exit(state):
    print("1. Újrapróbálod a játékot nyomozóként?")
    print("2. Kipróbálod a gyilkos történetét?")
    print("3. Kilépés a játékból.")
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.reset()  # Reset score
        detective_story(state)
    elif choice == "2":
        state.reset()  # Reset score
        killer_story(state)
    elif choice == "3":
        print("Köszönjük, hogy játszottál! Viszlát!")
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        retry_or_exit(state)


def first_meeting(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print(
            "\nA beszélgetés közben a pincértől elvesztek egy-egy pezsgős poharat, majd felhozod az öt évvel ezelőtt gyilkossági ügyet:")
        print("1. Váltig állítod, hogy Ron gyilkos és nem érted, hogy mászkálhat szabadon, így persze vitatkozni kezdtek.")
        print("2. Próbálsz Ron kedvére tenni, így úgy teszel, mintha aki nagyon sajnálja, hogy anno igazságtalanul vádolták meg a gyilkossággal.")
        print("Jelenlegi pontszámod:", state.get_score())
        return first_meeting_talk(state)
    elif choice == "2":
        state.update_score(5)
        print("\nOtthagyod a professzort és Ronékat és inkább körülnézel a hajón. Észreveszel egy házaspárt. Hogyan tovább?")
        print("\n1. Utánuk lopódzol és kihallgatod őket, mik a terveik.")
        print("2. Visszamész a szobádba.")
        print("Jelenlegi pontszámod:", state.get_score())
        return follow_the_couple(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)

def first_meeting_talk(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nMielőtt a vita elfajult volna, a professzor leállított. Otthagyod a professzort és Ronékat és inkább körülnézel a hajón. Észreveszel egy házaspárt. Hogyan tovább?")
        print("\n1. Utánuk lopódzol és kihallgatod őket, mik a terveik.")
        print("2. Visszamész a szobádba.")
        print("Jelenlegi pontszámod:", state.get_score())
        return follow_the_couple(state)
    elif choice == "2":
        state.update_score(0)
        print("\nRonnak gyanús lett a mézes-mázas viselkedésed. Elbuktál!")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)

def follow_the_couple(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nMeghallod, hogy a házaspár a házassági évfordulóját akarja ünnepelni. Tervet eszelsz ki:")
        print("1. Hangtorzítót használva rendelsz egy üveg bort a feleség nevében a hajó bárjába.")
        print("2. Szóbaelegyedsz a párral és csatlakozol hozzájuk.")
        print("Jelenlegi pontszámod:", state.get_score())
        return continue_planning(state)
    elif choice == "2":
        state.update_score(0)
        print("\nNem megy ez neked. Sajnálom, a játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)


def continue_planning(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nMiután a bort megrendelted, hívást kapsz Milótól, aki elmondja, hogy naponta egy gyilkosságot kell elkövetned addig, míg Ron rád nem talál. Mit teszel?")
        print("1. Teszel Milóra, élvezni akarod a hajóutat, ezért elmész a bárba.")
        print("2. Tovább sétálgatsz a hajón, lehetséges áldozatokat keresve.")
        print("Jelenlegi pontszámod:", state.get_score())
        return seaching_new_victim(state)
    elif choice == "2":
        state.update_score(0)
        print("\nCsatlakozol egy házaspárhoz??? Nem megy ez neked. Sajnálom, a játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)


def seaching_new_victim(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(0)
        print("\nKomolyan? Ellentmondtál a Moriarty-család fejének? Meghaltál. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)

    elif choice == "2":
        state.update_score(10)
        print("\nMiközben az első gyilkosság már a jelenléted nélkül lezajlott (a bor mérgezett volt, amit rendeltél), közben kiszúrtál még két párost, akikből jó áldozatok lesznek. Mit teszel?")
        print("1. Megtervezed a következő gyilkosságot.")
        print("2. Tovább nézelődsz, hogy jobban kiismerd magad a hajón.")
        print("Jelenlegi pontszámod:", state.get_score())
        return planning_murder(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)


def planning_murder(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nMegtervezted a következő gyilkosságot. Mindent előkészítettél és nyugovóra tértél. Másnap az ebédlőben újra összefutsz Ronnal és a társával. "
              "A változatosság kedvéért ismét belekötsz Ronba, de mielőtt elfajulna a vita sikítást hallotok, így Ronék kiszaladnak a hajótatra. Mit teszel?")
        print("1. A professzorral együtt utánuk mész.")
        print("2. Elhúzol onnan, mielőtt még gyanút fognának.")
        print("Jelenlegi pontszámod:", state.get_score())
        return second_murder(state)
    elif choice == "2":
        state.update_score(10)
        print("\nSzétnéztél is közben megtervezted a következő gyilkosságot. Mindent előkészítettél és nyugovóra tértél. Másnap az ebédlőben újra összefutsz Ronnal és a társával. "
              "A változatosság kedvéért ismét belekötsz Ronba, de mielőtt elfajulna a vita sikítást hallotok, így Ronék kiszaladnak a hajótatra. Mit teszel?")
        print("1. A professzorral együtt utánuk mész.")
        print("2. Elhúzol onnan, mielőtt még gyanút fognának.")
        print("Jelenlegi pontszámod:", state.get_score())
        return second_murder(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)


def second_murder(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nKözösen megvizsgáltátok a helyszínt és megállapítottátok, hogy a gyilkos szándékosan párokat vagy barátokat szemel ki magának, hogy olyan gyilkosságot hajtson végre, ahol"
              "tudtán kívül az egyik fél végez a másikkal. "
              "Ahhoz, hogy ne történhessen újabb gyilkosság, Ronnak és a társának egy napon belül meg kell találnia az informátort. Úgy döntenek, hogy elmondják nektek, "
              "hogy a Moriarty-család áll a gyilkosságok mögött és, hogy te vagy a professzor valószínűleg nekik dolgozik, ezért mind gyanúsak, de mivel az akadémián dolgoznak, "
              "segítsetek nekik a nyomozásban. Az akadémia egy másik professzora és egy volt diákja szintén a hajón tartózkodik, velük is megosztják ugyanezt."
              "Közösen arra jutottatok, hogy mind a hatan a hatodik emeleti bárba mentek, mert annak csak egy bejárata van, "
              "így senki nem tud észrevétlenül meglépni. Ám míg várakoztok, a doktor egy üzenetet talál, ami a harmadik gyilkosságra utal: éjfél után 10 perccel "
              "a .01-es szobában történik. Mit teszel?")
        print("1. Azt javaslod, hogy mindenki menjen és ellenőrizzen egy emeletet.")
        print("2. Jól elvagy itt a hatodikon, támogatod Ront, hogy maradjatok együtt.")
        print("Jelenlegi pontszámod:", state.get_score())
        return third_murder(state)
    elif choice == "2":
        state.update_score(0)
        print("\nAzzal, hogy leléptél csak gyanúsabb lettél. Lebuktál és elkaptak. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)


def third_murder(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nRon nem értett egyet azzal, hogy szétváljatok, de végül rábólintott. Te a harmadik emeleten ellenőrzöd a 301-es szobát. Mindenki elmegy ellenőrizni az emeletét."
              "Amikor végeztetek, visszamentek a hatodikra, de Ront és a társát a hetedik emeleti medencénél találjátok. Megmentették az újabb áldozatokat, most pedig arról kérdeznek, hogy"
              "ki-mit tapasztalt a szobák ellenőrzésénél. Mit felelsz?")
        print("1. Nem volt semmi különös. Kicsit rád förmedtek, de egyébként nem történt semmi.")
        print("2. A szoba üres volt.")
        print("Jelenlegi pontszámod:", state.get_score())
        return pool_murder(state)
    elif choice == "2":
        state.update_score(0)
        print("\nAzzal, hogy támogattad Ront, magadra terelted a gyanút. Elbuktál. A játék véget ért.")
        print("Az elért pontszámod:", state.get_score())
        return retry_or_exit(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)


def pool_murder(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(10)
        print("\nRon hirtelen azt mondja, hogy hamarosan fényt derít a gyilkos kilétére és arra kéri négyötöket, hogy maradjatok ott a medencénél. Ő és a társa pedig kimentek a helyiségből, "
              "hogy telefonáljanak. Ezidő alatt, de elaltod a másik három tagot, majd Ronék után mész és őket is kiütöd. Egy színházterembe viszel mindenkit, ahol épp egy bűvészműsor zajlik, amikor"
              "Ron magához tér. "
              "A színpadon a bűvész felemeli azt a fegyvert, amit még Milo rejtetett el a szobájukban azért, hogy Ron azzal végezzen majd veled. "
              "Megakadályozza, hogy a bűvész elsüsse az igazi fegyvert és közben észrevesz titetek, akik eszméletlenül ültök az első sorban. Megjelenik Milo, aki kíváncsian várja, "
              "rájött-e arra, ki a gyilkos és egyben az informátor. Ron Fin professzora szegezi a fegyvert és azt állítja ő az. Mit teszel?")
        print("1. Megmented a professzort.")
        print("2. Nem teszel semmit.")
        print("Jelenlegi pontszámod:", state.get_score())
        return get_away_murder(state)
    elif choice == "2":
        state.update_score(0)
        print("\nRon hirtelen azt mondja, hogy hamarosan fényt derít a gyilkos kilétére és arra kéri négyötöket, hogy maradjatok ott a medencénél. Ő és a társa pedig kimentek a helyiségből, "
              "hogy telefonáljanak. Ezidő alatt, de elaltod a másik három tagot, majd Ronék után mész és őket is kiütöd. Egy színházterembe viszel mindenkit, ahol épp egy bűvészműsor zajlik, amikor"
              "Ron magához tér. "
              "A színpadon a bűvész felemeli azt a fegyvert, amit még Milo rejtetett el a szobájukban azért, hogy Ron azzal végezzen majd veled. "
              "Megakadályozza, hogy a bűvész elsüsse az igazi fegyvert és közben észrevesz titetek, akik eszméletlenül ültök az első sorban. Megjelenik Milo, aki kíváncsian várja, "
              "rájött-e arra, ki a gyilkos és egyben az informátor. Ron Fin professzora szegezi a fegyvert és azt állítja ő az. Mit teszel?")
        print("1. Megmented a professzort.")
        print("2. Nem teszel semmit.")
        print("Jelenlegi pontszámod:", state.get_score())
        return get_away_murder(state)
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(state)

def get_away_murder(state):
    choice = input("Választásod: ").strip()

    if choice == "1":
        state.update_score(50)
        print("A végső pontszámod:", state.get_score())
        return
    elif choice == "2":
        state.update_score(0)
        print("A végső pontszámod:", state.get_score())
        return
    else:
        print("Érvénytelen választás. Kérlek, próbáld újra.")
        killer_story(choice)
