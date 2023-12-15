from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper

# Initialize Data_Wrapper and LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def staff_schedule_menu(return_to_main_menu):
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
    all_employees = data_wrapper.get_all_employees()
    for employee in all_employees:
        print(f"{employee.id}: {employee.name}, {employee.title}")

def create_cabin_crew():
    print("Create New Cabin Crew Member")
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    cell_phone = input("Enter Cell Phone: ")
    email = input("Enter Email: ")
    title = input("Enter Title: ")
    home_phone = input("Enter Home Phone (optional): ")


    logic_wrapper.add_employee(id, name, address, cell_phone, email, title, home_phone)
    print("Cabin crew member added successfully.")

def modify_schedule():
    pass    # placeholder

def view_staff_not_working():
    pass    # placeholder

def view_staff_working():
    pass    # placeholder

def search_flight_crew():
    pass    # placeholder

# Replace this with the actual function or way you return to the main menu
def return_to_main_menu():
    pass

# Example: Start the staff schedule menu
staff_schedule_menu(return_to_main_menu)