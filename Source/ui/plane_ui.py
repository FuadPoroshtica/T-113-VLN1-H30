# plane_ui.py

def planes_menu(return_to_main_menu):
    while True:
        print("Planes Menu")
        print("-----------")
        print("1. Modify Planes")
        print("2. Create New Plane")
        print("M. Return to Main Menu")
        print("B. Go Back")
        print("Q. Quit")

        choice = input("Select option: ").upper()

        if choice == '1':
           pass  # placeholder
        elif choice == '2':
            pass  # placeholder
        elif choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            return_to_main_menu()
            break   # placeholder
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")
