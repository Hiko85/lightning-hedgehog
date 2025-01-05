#Főmodul

from detective.detective import detective_main
from hamster.hamster import hamster_start
from hamster.hamster_logic import *
import tic_tac_toe

def main_menu():
    choice = ""
    
    while choice != "4":
        print("\nÜdvözlünk a játékban! Válassz az alábbi opciók közül:")
        print("1. Hörcsög Tamagotchi")
        print("2. Nyomozós játék")
        print("3. Amőba játék")
        print("4. Kilépés")

        choice = input("Add meg a választásod (1-4): ").strip()

        if choice == "1":
            print("\nHörcsög Tamagotchi indítása...\n")
            start_hamster_tamagotchi()
        elif choice == "2":
            print("\nNyomozós játék indítása...\n")
            start_detective()
        elif choice == "3":
            print("\nAmőba játék indítása...\n")
            start_tic_tac_toe()
        elif choice == "4":
            print("Köszönjük, hogy játszottál! Viszlát!")
        else:
            print("Érvénytelen választás. Kérlek, próbáld újra.")

def start_hamster_tamagotchi():
    print("Hamarosan érkezik a Hörcsög Tamagotchi játék!")
    hamster_start()

def start_detective():
    print("Hamarosan érkezik a Nyomozós játék!")
    detective_main() # Nyomozós játék indítása
   
def start_tic_tac_toe():
    print("Hamarosan érkezik az Amőba játék!")
    tic_tac_toe
      
main_menu()
input("\nNyomj egy gombot a kilépéshez...")