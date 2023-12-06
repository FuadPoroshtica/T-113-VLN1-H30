# plane_ui.py

def planes_menu(return_to_main_menu):
    while True:
        print("\nPlanes Menu")
        print("-----------")
        print("1. Modify Planes")
        print("2. Create New Plane")
        print("M. Return to Main Menu")
        print("B. Go Back")
        print("Q. Quit")

        choice = input("Select option: ").upper()

        if choice == '1':
            print("Modify Planes Placeholder")  # Placeholder for modifying planes
        elif choice == '2':
            print("Create New Plane Placeholder")  # Placeholder for creating a new plane
        elif choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            # Here you would implement the logic to go back to the previous screen.
            # If this is the first screen after main menu, 'B' could behave the same as 'M'.
            return_to_main_menu()
            break
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")
