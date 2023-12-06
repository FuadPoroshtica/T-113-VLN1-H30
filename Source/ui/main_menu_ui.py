# main_menu.py

from ui.plane_ui import planes_menu
from ui.location_ui import locations_menu


def login_screen():
    while True:
        print("Login Screen")
        print("------------")
        print("Login (press L)")
        print("Quit (press Q)")

        choice = input("Select option: ").upper()

        if choice == 'L':
            main_menu()  # This will now take the user to the main menu
        elif choice == 'Q':
            exit()
        else:
            print("Invalid choice. Please choose again.")

def main_menu():
    while True:
        print("Main Menu")
        print("1. Locations")  
        print("2. Flight crew")
        print("3. Planes")
        print("4. Flight schedule")
        print("5. Staff schedule")
        print("6. Logout")
        print("Q. Quit")

        choice = input("Select option: ").upper()

        if choice == '1':
            if choice == '1':
                locations_menu(main_menu)
        elif choice == '2':
            pass  # placeholder
        elif choice == '3':
            planes_menu(main_menu)
        elif choice == '4':
            pass  # placeholder
        elif choice == '5':
            pass  # placeholder
        elif choice == '6':
            login_screen() 
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")
