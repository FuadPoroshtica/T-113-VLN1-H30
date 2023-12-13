def flight_crew_menu(return_to_main_menu):
    while True:
        print("Flight Crew Menu")
        print("----------------")
        print("1. Pilots")
        print("2. Stewards")
        print("3. Search for ID")
        print("4. Create Cabin Crew Plan")
        print("5. Make a new Pilot")
        print("6. Make a new Steward")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            view_pilots()
        elif choice == '2':
            view_stewards()
        elif choice == '3':
            search_for_id()
        elif choice == '4':
            create_cabin_crew_plan()
        elif choice == '5':
            create_new_pilot()
        elif choice == '6':
            create_new_steward()
        elif choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            return_to_main_menu()
            break
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

def view_pilots():
    pass    #placeholder

def view_stewards():
    pass    #placeholder

def search_for_id():
    pass    #placeholder

def create_cabin_crew_plan():
    pass    #placeholder
def create_new_pilot():
    pass    #placeholder

def create_new_steward():
    pass    #placeholder
