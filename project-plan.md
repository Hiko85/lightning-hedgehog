# Csapatnév: Villámsündisznók

## Projekt rövid bemutatása:
###**A projekt neve

###**Cél:
A projekt célja az alapvető programozási fogalmak és technikák alkalmazásának bemutatása (például: változók, ciklusok, feltételek, függvények).
###**Fejlesztési környezet:
Python 3.12
IDE: Visual Studio Code
Használt könyvtárak: math, random, os

##** Program rövid bemutatása:
##Cél:

##Felhasználói felület: 
Egyszerű terminál alapú megoldás, amely megjeleníti a játék állapotát és kommunikál a játékosokkal.
- név bekéréssel kezdjük
- print (Üdv, xy! )
- esetleg jelszót generáltatunk vele
- megkérdezzük, mit szeretne csinálni? játszani vagy tanulni?
  - kiírni a választható opciókat:
  - Válassz az alábbiakból, hogy mit szeretnél csinálni:
    - Tanulni?
    - Játszani?
  - A játékot választottad. Mivel játszanál?
    - amőba
    - hörcsög tamagochi
    - kalandjáték
###A választható játékok:
- Amőba játék- alapkoncepció:
Két játékos számára készül, ahol a játékosok felváltva adhatják meg, hová szeretnék elhelyezni jelölésüket (X vagy O) a 3x3-as táblán.
A program automatikusan ellenőrzi, hogy van-e nyertes, és pontot számol, ha valaki három egymást követő jelet helyez el sorban, oszlopban vagy átlósan.
- Hörcsög Tamagotchi – alapkoncepció
  - A hörcsögnek van egy vízszintje, ami folyamatosan csökken.
  -	A játékos bizonyos időközönként adhat vizet a hörcsögnek.
  -	Ha a vízszint túl alacsony lesz, a hörcsög kiszárad.
  -	Ha a játékos rendszeresen ad elegendő vizet, a hörcsög egészséges marad
- Kalandjáték – alapkoncepció: valami történetet elkezdünk, ahol bizonyos pontokon a felhasználó dönti el, hogy merre tovább, de előtte még ki kell választania, hogy a történetben ki akar lenni: a nyomozó vagy a gyilkos?
  -	Nyomozóként: A játékos nyomokat gyűjt és megpróbálja kitalálni, ki a gyilkos.
  -	Gyilkosként: A játékos elkövet egy bűncselekményt, majd próbálja elkerülni a lebukást.
  -	A játék interaktív, a játékos döntései változtatják a történetet.
    
  - A tanulást választottad. Matekoznál vagy inkább történelmi ismereteidet ellenőriznéd?
    - Matek
    - Történelem
###A választható tanuló modulok:
a. Matekozni szeretnék:
  -	kör sugara feladat,
  -	páros-páratlan,
  -	oszthatóság,
  -	másodfokú egyenlet,
  -	szorzótábla,
  -	prím számok,
  -	armstrong számok

b. Törizni szeretnék
  -	aranybulla,
  -	ilyen-olyan felkelés,
  -	xy uralkodó mettől-meddig uralkodott?
    
##Játék logika: 
Ellenőrzi a győzelmi feltételeket és biztosítja, hogy a mezők csak egyszer használhatók.

##Játék állapot: 
Nyomon követi a játék menetét, beleértve a játékosok pontszámát és a tábla aktuális állapotát.




--------------------------------------

## A megvalósított funkciók:
Funkcionalitás 
  milyen funkciókat szeretnénk pl. bekérem a felhasználótól az adatait, mit szeretne? játszani vagy tanulni?
  amit szeretnénk, hogy tudjon

## Modul lista (hogy mi az, ami benne van)
 - ki-melyiket fejleszti?
Modulok: Felhasználói felület, Játék logika, Játék állapot (de ha mi három játékot szeretnénk, akkor ez hogy alakul? és ott van a tanulós modul is)


  
*3. Chatbottal beszélgetnék:*
-	legalább 10 különböző parancsra tudjon válaszolni a bot

- valami feladatot kitalálni, ami listát gyűjt

adatok – kommunikáció - algoritmus

###Referenciának:
https://okt.inf.szte.hu/python-programozas/gyakorlat/szorgalmi-projekt/
http://tehetseg.inf.elte.hu/jegyzetek/HBakonyi_versenyfeladatok_python.pdf
https://miskei.hu/python/python_gyakorlo/index.html
