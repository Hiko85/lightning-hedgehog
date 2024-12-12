#Főmodul

import detective
import hamster
import tic_tac_toe

def main_menu():
    choice = ""
    
    while choice != "4":
        print("\nÜdvözlünk a játékban! Válassz az alábbi opciók közül:")
        print("1. Hörcsög Tamagotchi (hidratálás)")
        print("2. Kalandjáték (nyomozó vagy gyilkos)")
        print("3. Amőba játék")
        print("4. Kilépés")

        choice = input("Add meg a választásod (1-4): ").strip()

        if (choice) == "1":
            print("\nHörcsög Tamagotchi indítása...\n")
            start_hamster_tamagotchi()
        elif choice == "2":
            print("\nKalandjáték indítása...\n")
            start_detective_game()
        elif choice == "3":
            print("\nAmőba játék indítása...\n")
            start_tic_tac_toe()
        elif choice == "4":
            print("Köszönjük, hogy játszottál! Viszlát!")
        else:
            print("Érvénytelen választás. Kérlek, próbáld újra.")

def start_hamster_tamagotchi():
    print("Hamarosan érkezik a Hörcsög Tamagotchi játék!")
    hamster

def start_detective_game():
    print("Hamarosan érkezik a Kalandjáték!")
    detective
   
def start_tic_tac_toe():
    print("Hamarosan érkezik az Amőba játék!")
    tic_tac_toe
      
main_menu()