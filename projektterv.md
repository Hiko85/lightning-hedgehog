# IKT Projektmunka Dokumentáció
________________________________________
## Projekt címe: Python Játékok
Mini játékgyűjtemény Pythonban

Készítette: Orosz Adrienn, Oszlánszki Ildikó, Márkovits Marcella
________________________________________
## 1. A program célja
A projekt célja három különböző típusú játék kifejlesztése Python nyelven, amelyek egy közös főmenüből érhetők el. A program fejlesztése során a tanult algoritmusokat és programozási módszereket alkalmaztuk, különös figyelmet fordítva a moduláris kódstruktúrára, az olvashatóságra, valamint a felhasználói élményre.
A három játék:
1.	Hörcsög Tamagotchi: A játékos feladata, hogy gondoskodjon egy hörcsögről, különösen a megfelelő hidratálásáról.
2.	Nyomozós játék: Egy történetvezérelt játék, amelyben a játékos kiválaszthatja szerepét (nyomozó vagy gyilkos), és döntésein keresztül haladhat előre a történetben.
3.	Amőba: Klasszikus kétjátékos stratégiai játék, amelyben cél a három jel egymás melletti elhelyezése (sorban, oszlopban vagy átlósan).
________________________________________
## 2. Felhasználói útmutató
### 1.	Program elindítása:
A program futtatásához a games.py fájlt kell elindítani.
### 2.	Főmenü:
A program indításakor megjelenik egy főmenü, amelyben a következő lehetőségek közül választhat:
- 1: Hörcsög Tamagotchi
- 2: Nyomozós játék
- 3: Amőba
- 0: Kilépés
### 3.	Játékok elérése:
A választás után a megfelelő játék elindul, ahol a felhasználó a megjelenő utasításokat követve haladhat előre.
### 4.	Kilépés:
A játékok befejezése után a játékos visszatérhet a főmenübe, vagy megnyomhatja az Enter-t a teljes programból való kilépéshez.
________________________________________
## 3. Modulok
A program több modulból áll, mindegyik modul külön fájlban található. A modulok célja a funkcionalitás és a játéklogika elkülönítése.
- **games.py:** <br>Ez a főfájl, amely a főmenüt és az alapvető vezérlési logikát tartalmazza. Meghívja a megfelelő modulokat az egyes játékok futtatására.
---
- **hamster.py:** <br>Ez tartalmazza a hivatkozásaokat, amelyek a "hamster_logic"-ból hívja meg a függvényeket.
- **hamster_logic.py:** <br>A Hörcsög játékkal kapcsolatos logikát tartalmazza. Ez a modul kezeli a játék teljes logikai folyamatát.
---
- **detective_user.py:** <br>Bekéri a játékostól a választásait.
- **detective_logic.py:** <br>A játék logikáját kezeli, és az állapotot detective_state.py fájlban frissíti. A nyomozónak és a gyilkosnak kiosztja, hogy kapott-e vagy veszített pontot.
- **detective_state.py:** <br>A nyomozó és a gyilkos állapota, a pontokot számolja vagy újrakezdés esetén visszaállítja. A kalandjáték változóit tartalmazza.
- **detective.py:** <br>a fő program, ami meghatározza a játék menetét és a játékos választásai alapján kezeli a logikát.
---
- **tic_tac_toe.py:** <br>Elindítja a játékot def main_menu.
- **tic_tac_toe_user.py:** <br>Bekéri az aktuális játékostól a következő lépést.
- **tic_tac_toe_logic.py:** <br>Az Amőba játék szabályait és logikáját kezeli. Ellenőrzi, hogy nyert-e valamelyik játékos és hogy tele van-e a tábla. 
- **tic_tac_toe_state.py:** <br>Ez a modul a játék állapotát kezeli. inicializálja a játék allapotát és megjelínit a táblát. Az Amőba mezőinek állapotát tárolja.
________________________________________
Funkció
     Hörcsög, Amőba, Nyomozó:
- Ciklusok:
     - while a menüstruktúrában és a játékok folyamatos futtatásához.
- Feltételes utasítások:
     - if-elif-else a felhasználói döntések kezeléséhez.
- Listák:
     - Az Amőba játéktábla állapotának nyomon követésére.
- Eljárások, függvények:
     - A logika strukturált megvalósítására.
________________________________________
## 4. A játék működési folyamata
1.	Főmenü:
A felhasználó beír egy számot a kívánt opció kiválasztásához.
2.	Játék indítása:
A választott modul inicializálódik, és a felhasználónak egyedi utasítások jelennek meg.
3.	Pontszámítás és eredmény:
A játékokban gyűjtött pontok vagy az aktuális nyertes megjelenik a játék végén.
4.	Kilépés:
A játék végén a felhasználónak lehetősége van a programból való kilépésre.
________________________________________
## 5. Telepítési és futtatási lépések
1.	Python telepítése:
A program futtatásához Python 3.8 vagy újabb verzió szükséges.
2.	Fájlok letöltése:
A projekt összes fájlja letölthető a GitHub-tárhelyről.
3.	Futtatás:
Navigáljon a projekt könyvtárába, és futtassa a következő parancsot:
bash
**python main.py**
________________________________________
## 6. Fejlesztési folyamat
A csapat minden tagja külön-külön fejlesztett egy játékot. A közös munkát GitHub használatával koordináltuk, a változásokat commitok formájában dokumentáltuk.
________________________________________
## 7. Továbbfejlesztési lehetőségek
1.	Online multiplayer mód hozzáadása az Amőbához.
2.	A Nyomozó játék történetének kibővítése több választási lehetőséggel, történéssel, végkifejlettel.
3.	Grafikus felhasználói felület (GUI) megvalósítása.
________________________________________


## A struktúra
1.	**games.py:** Ez a főfájl, amely a főmenüt és az alapvető vezérlési logikát tartalmazza.
2.	A *_user.py felelős a felhasználói interakciókért.
- Meghívja a megfelelő *_logic.py fájlokat.
3.	A *_logic.py modulok a játékmenetet irányítják.
- Az állapotot módosítják a hozzájuk tartozó *_state.py modulban.
4.	A *_state.py modulok tárolják az aktuális játék változóit.
- Ez biztosítja, hogy minden állapot jól elkülönített legyen.

Felhasználói felület modul: Ez a *_user.py, amely kezeli a játékos interakcióit és a játékok közötti navigációt. Itt történik a menü és a játékos döntéseinek megjelenítése.
Játék logika modul: Ez tartalmazza a játékmenet működését (szabályok, döntések, események). Minden játéknak külön fájlban kell lennie, például: hamster_logic.py, detective_logic.py, tic_tac_toe_logic.py.
Játék állapot modul: Ez kezeli az adott játék változóit és állapotát. Itt tároljuk például a hörcsög hidratáltságát, a játékos pontszámát, vagy az Amőba mezőinek állapotát. Minden játékhoz egy külön modulban tároljuk az állapotot, például: hamster_state.py, detective_state.py, tic_tac_toe_state.py.

