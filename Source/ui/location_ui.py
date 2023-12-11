# location_ui.py
from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack

def locations_menu():

    menu_stack.append(locations_menu)
    while True:
        print("\nLocations Menu")
        print("---------------")
        print("1. Create New Location")
        print("2. Modify Location")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            create_location() 
        elif choice == '2':
            modify_location()  
        elif choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            return_to_previous_menu()
            break
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

def print_locations():
    pass    # placeholder

def create_location():
    pass    # placeholder

def modify_location():
    pass    # placeholder
