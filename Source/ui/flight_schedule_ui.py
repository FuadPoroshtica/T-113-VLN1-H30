def flight_schedule_menu(return_to_main_menu):
  
    while True:
        print("Flight Schedule Menu")
        print("--------------------")
        print("1. Create new flight schedule")
        print("2. Modify flight schedule")
        print("3. Search for flight")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            create_flight_schedule()
        elif choice == '2':
            modify_flight_schedule()
        elif choice == '3':
            search_for_flight()
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

def print_flight_schedule():
    pass

def create_flight_schedule():
    pass

def modify_flight_schedule():
    pass

def search_for_flight():
    pass