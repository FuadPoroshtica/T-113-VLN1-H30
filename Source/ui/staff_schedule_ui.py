def staff_schedule_menu(return_to_main_menu):
    # Display the current staff schedule
    print_staff_schedule()

    while True:
        print("\nStaff Schedule Menu")
        print("--------------------")
        print("1. Modify Schedule")
        print("2. Create cabin crew")
        print("3. Staff not working")
        print("4. Staff working")
        print("5. Search flight crew")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            modify_schedule()
        elif choice == '2':
            create_cabin_crew()
        elif choice == '3':
            view_staff_not_working()
        elif choice == '4':
            view_staff_working()
        elif choice == '5':
            search_flight_crew()
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

def print_staff_schedule():
    pass    # placeholder 

def modify_schedule():
    pass    # placeholder

def create_cabin_crew():
    pass    # placeholder

def view_staff_not_working():
    pass    # placeholder

def view_staff_working():
    pass    # placeholder

def search_flight_crew():
    pass    # placeholder