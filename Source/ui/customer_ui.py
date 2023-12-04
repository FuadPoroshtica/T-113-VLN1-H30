from logic.customer_logic import Customer_Logic
from model.customer import Customer
from ui.input_validators import *

class Customer_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("customer menu")
        print("1. create customer")
        print("2. list all customers")
        print("b. to go back")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command:")
            command = command.lower()
            if command == "b":
                print("going back")
                return "b"
            elif command == "q":
                print("quitting")
                return "q"
            elif command == "1":
                c = Customer()
                while True:
                    c.name = input("Enter the name of the customer: ")
                    try:
                        validate_name(c.name)
                        break
                    except NameLengthException:
                        print("name was too long")
                    except:
                        print("some error")
                c.birth_year = input("Enter the birth year of the customer: ")
                self.logic_wrapper.create_customer(c)
            elif command == "2":
                result = self.logic_wrapper.get_all_customers()
                for elem in result:
                    print(f"name: {elem.name}, birth year: {elem.birth_year}")
            else:
                print("invalid input, try again")
        