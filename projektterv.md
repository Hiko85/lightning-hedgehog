#IKT Projektmunka Dokumentáció
________________________________________
##Projekt címe: Python Játékok
Mini játékgyűjtemény Pythonban
Készítette: Orosz Adrienn, Oszlánszki Ildikó, Márkovits Marcella
________________________________________
##1. A program célja
A projekt célja három különböző típusú játék kifejlesztése Python nyelven, amelyek egy közös főmenüből érhetők el. A program fejlesztése során a tanult algoritmusokat és programozási módszereket alkalmaztuk, különös figyelmet fordítva a moduláris kódstruktúrára, az olvashatóságra, valamint a felhasználói élményre.
A három játék:
1.	Hörcsög Tamagotchi: A játékos feladata, hogy gondoskodjon egy hörcsögről, különösen a megfelelő hidratálásáról.
2.	Kalandjáték: Egy történetvezérelt játék, amelyben a játékos kiválaszthatja szerepét (nyomozó vagy gyilkos), és döntésein keresztül haladhat előre a történetben.
3.	Amőba: Klasszikus kétjátékos stratégiai játék, amelyben cél a három jel egymás melletti elhelyezése (sorban, oszlopban vagy átlósan).
________________________________________
##2. Felhasználói útmutató
###1.	Program elindítása:
A program futtatásához a jatekok.py fájlt kell elindítani.
###2.	Főmenü:
A program indításakor megjelenik egy főmenü, amelyben a következő lehetőségek közül választhat:
o	1: Hörcsög Tamagotchi
o	2: Kalandjáték
o	3: Amőba
o	0: Kilépés
###3.	Játékok elérése:
A választás után a megfelelő játék elindul, ahol a felhasználó a megjelenő utasításokat követve haladhat előre.
###4.	Kilépés:
A játékok befejezése után a játékos visszatérhet a főmenübe, vagy megnyomhatja az Enter-t a teljes programból való kilépéshez.
________________________________________
##3. Modulok
A program több modulból áll, mindegyik modul külön fájlban található. A modulok célja a funkcionalitás és a játéklogika elkülönítése.
jatekok.py:
Ez a főfájl, amely a főmenüt és az alapvető vezérlési logikát tartalmazza. Meghívja a megfelelő modulokat az egyes játékok futtatására.
hörcsög_felhasznalo.py:
Bekéri a játékostól, hogy mit szeretne adni a hörcsögnek.
hörcsög_logika.py:
A Hörcsög játékkal kapcsolatos logikát tartalmazza. Ez a modul kezeli a játék logikai folyamatát, és a hörcsög_jatek_allapot.py modulban tárolt állapotokat frissíti.
hörcsög_jatek_allapot.py:
A Hörcsög aktuális állapotát adja vissza. 
kaland_felhasznalo.py:
Bekéri a játékostól a választásait.
kaland_logika.py:
A kalandjáték logikáját kezeli, és az állapotot kaland_jatek_allapot.py fájlban frissíti. A nyomozónak és a gyilkosnak kiosztja, hogy kapott-e vagy veszített pontot.
kaland_jatek_allapot.py:
A nyomozó és a gyilkos állapota. A kalandjáték változóit tartalmazza.
amőba_felhasznalo.py:
Bekéri az aktuális játékostól a következő lépést.
amőba_logika.py:
Az Amőba játék szabályait és logikáját kezeli. Ellenőrzi, hogy nyert-e valamelyik játékos és hogy tele van-e a tábla. 
amőba_jatek_allapot.py:
Ez a modul a játék állapotát kezeli, például a tábla megjelenítése. Az Amőba mezőinek állapotát tárolja.

Funkció
     Hörcsög, Amőba, Kaland:
•	Ciklusok:
o	while a menüstruktúrában és a játékok folyamatos futtatásához.
•	Feltételes utasítások:
o	if-elif-else a felhasználói döntések kezeléséhez.
•	Listák:
o	Az Amőba játéktábla állapotának nyomon követésére.
•	Eljárások, függvények:
o	A logika strukturált megvalósítására.
________________________________________
##4. A játék működési folyamata
1.	Főmenü:
A felhasználó beír egy számot a kívánt opció kiválasztásához.
2.	Játék indítása:
A választott modul inicializálódik, és a felhasználónak egyedi utasítások jelennek meg.
3.	Pontszámítás és eredmény:
A játékokban gyűjtött pontok vagy az aktuális nyertes megjelenik a játék végén.
4.	Kilépés:
A játék végén a felhasználónak lehetősége van a programból való kilépésre.
________________________________________
##5. Telepítési és futtatási lépések
1.	Python telepítése:
A program futtatásához Python 3.8 vagy újabb verzió szükséges.
2.	Fájlok letöltése:
A projekt összes fájlja letölthető a GitHub-tárhelyről.
3.	Futtatás:
Navigáljon a projekt könyvtárába, és futtassa a következő parancsot:
bash
Kód másolása
python main.py
________________________________________
##6. Fejlesztési folyamat
A csapat minden tagja külön-külön fejlesztett egy játékot. A közös munkát GitHub használatával koordináltuk, a változásokat commitok formájában dokumentáltuk.
________________________________________
##7. Továbbfejlesztési lehetőségek
1.	Online multiplayer mód hozzáadása az Amőbához.
2.	A Kalandjáték történetének kibővítése többféle végkifejlettel.
3.	Grafikus felhasználói felület (GUI) megvalósítása.
________________________________________


##A struktúra
1.	jatekok.py: Ez a főfájl, amely a főmenüt és az alapvető vezérlési logikát tartalmazza.
2.	A *_felhasznalo.py felelős a felhasználói interakciókért.
o	Meghívja a megfelelő *_logika.py fájlokat.
3.	A *_logika.py modulok a játékmenetet irányítják.
o	Az állapotot módosítják a hozzájuk tartozó *_allapot.py modulban.
4.	A *_allapot.py modulok tárolják az aktuális játék változóit.
o	Ez biztosítja, hogy minden állapot jól elkülönített legyen.

Felhasználói felület modul: Ez a *_felhasznalo.py, amely kezeli a játékos interakcióit és a játékok közötti navigációt. Itt történik a menü és a játékos döntéseinek megjelenítése.
Játék logika modul: Ez tartalmazza a játékmenet működését (szabályok, döntések, események). Minden játéknak külön fájlban kell lennie, például: hörcsög_logika.py, kaland_logika.py, amőba_logika.py.
Játék állapot modul: Ez kezeli az adott játék változóit és állapotát. Itt tároljuk például a hörcsög hidratáltságát, a játékos pontszámát, vagy az Amőba mezőinek állapotát. Minden játékhoz egy külön modulban tároljuk az állapotot, például: hörcsög_allapot.py, kaland_allapot.py, amőba_allapot.py.

