# from logic.customer_logic import Customer_Logic
# from model.customer import Customer
# from ui.customer_ui import Customer_UI
# from logic.logic_wrapper import Logic_Wrapper


"""class MainMenu_UI:
    def menu_output(self):
        print("Main Menu")
        print("1. Locations")
        print("2. Flight Crew")
        print("3. Planes")
        print("4. Flight Schedule")
        print("5. Staff Schedule")
        print("6. Logout")
        print("q. Quit")

    def input_prompt(self):
        user_input = input("Select option: ")"""


from ui.plane_ui import planes_menu

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
            pass  # Placeholder for Locations functionality
        elif choice == '2':
            pass  # Placeholder for Flight crew functionality
        elif choice == '3':
            planes_menu(main_menu)  # Go to the planes menu
        elif choice == '4':
            pass  # Placeholder for Flight schedule functionality
        elif choice == '5':
            pass  # Placeholder for Staff schedule functionality
        elif choice == '6':
            login_screen()  # This will now take the user back to the login screen
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

