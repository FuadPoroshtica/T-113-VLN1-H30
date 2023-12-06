# from logic.customer_logic import Customer_Logic
# from model.customer import Customer
# from ui.customer_ui import Customer_UI
# from logic.logic_wrapper import Logic_Wrapper


class MainMenu_UI:
    def __init__(self):
        pass

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
        input = input("Select option: ")
