# employees_ui.py
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper

# Initialize Data_Wrapper and LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def employees_menu(return_to_main_menu):
    while True:
        print("\nEmployees menu")
        print("--------------------")
        print("1. View all employees")
        print("2. Add employees")
        print("3. Modify employees")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            view_all_employees()
        elif choice == '2':
            add_employees()
        elif choice == '3':
            modify_employees()
        elif choice in ['M', 'B']:
            return_to_main_menu()
            break
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

def view_all_employees():
    while True:
        all_employees = logic_wrapper.get_all_employees()
        print("\nList of All Employees:")
        print("----------------------")
        for employee in all_employees:
            print(f"{employee.id}: {employee.name}, {employee.title}")

        print("\nMain Menu (M), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == 'M':
            break
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

def add_employees():
    print("\nAdd a new employee")
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    cell_phone = input("Enter Cell Phone: ")
    email = input("Enter Email: ")
    title = input("Enter Title: ")
    home_phone = input("Enter Home Phone (optional): ")

    logic_wrapper.add_employee(id, name, address, cell_phone, email, title, home_phone)
    print("Employee added successfully.")

def modify_employees():
    print("\nModify an Employee's Details")
    employee_id = input("Enter the ID of the employee to modify: ")

    employee = logic_wrapper.get_employee_by_id(employee_id)
    if employee is None:
        print("No employee found with the given ID.")
        return

    print(f"Modifying details for employee {employee.name} (ID: {employee.id})")
    new_details = {
        'cell_phone': input(f"Enter new cell phone number (current: {employee.cell_phone}): ") or None,
        'email': input(f"Enter new email address (current: {employee.email}): ") or None,
        'home_phone': input(f"Enter new home phone (current: {employee.home_phone}): ") or None,
        'address': input(f"Enter new home address (current: {employee.address}): ") or None
    }

    if logic_wrapper.is_employee_a_pilot(employee_id):
        new_details['plane_licenses'] = input(f"Enter new pilot licenses (current: {employee.plane_licenses}): ") or None

    logic_wrapper.update_employee_details(employee_id, new_details)
    print("Employee details updated successfully.")

# Replace this with the actual function or way you return to the main menu
def return_to_main_menu():
    pass