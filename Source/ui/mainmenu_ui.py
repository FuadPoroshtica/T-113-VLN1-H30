from logic.customer_logic import Customer_Logic
from model.customer import Customer
from ui.customer_ui import Customer_UI
from logic.logic_wrapper import Logic_Wrapper

class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print("main menu")
        print("1. customer menu")
        print("2. car menu")
        print("q. to exit")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command:")
            command = command.lower()
            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                menu = Customer_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                pass
            else:
                print("invalid input, try again")
            