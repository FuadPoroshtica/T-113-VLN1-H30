# employees_ui.py
from model.employee_model import Employee
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from ui.interface_ui import interface
from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack, handle_menu_options

# Initialize Data_Wrapper and LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)


def employees_menu():
    menu_stack.append(employees_menu)
    while True:
        content = [
            "Employees menu",
            "--------------------",
            "1. View all employees",
            "2. Add employees",
            "3. Modify employees",
            "Main Menu (M), Back (B), Quit (Q)"
        ]
        interface(content)
        choice = input("Select option: ").upper()

        if choice == "1":
            view_all_employees()
        elif choice == "2":
            add_employees()
        elif choice == "3":
            modify_employees()
        elif choice == "M":
            return_to_main_menu()
            break
        elif choice == "B":
            return_to_previous_menu()
            break
        elif choice == "Q":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")


def view_all_employees():
    menu_stack.append(view_all_employees)
    all_employees = logic_wrapper.get_all_employees()

    content = [
        "List of All Employees:",
        "----------------------",
        *["ID: {:<10}, Name: {:<20}, Title: {:<15}, Address: {:<25}, Cell: {:<15}, Email: {:<25}, Home Phone: {:<15}, Current Trip: {:<15}, Lincenses: {} ".format(employee.id, employee.name, employee.title, employee.address, employee.cell_phone, employee.email, employee.home_phone, employee.current_trip, employee.plane_licenses) for employee in all_employees]
    ]
    interface(content)
    handle_menu_options()


def add_employees():
    print("\nAdd a new employee")
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    address = input("Enter Home Address: ")
    cell_phone = input("Enter Cell Phone: ")
    email = input("Enter Email: ")
    title = input("Enter Title: ")
    home_phone = input("Enter Home Phone (optional): ")
    plane_licenses="None"
    if title.lower() == "pilot":
        plane_licenses = add_license()

    new_employee = Employee(id, name, address, cell_phone, email, title, home_phone,plane_licenses=plane_licenses)


    status=logic_wrapper.add_employee(new_employee)
## vinsamlegst gefið þessu sinn eigin glugga/function
    if type(status) == type([]): #prentar errors
        print("\n")
        for x in status:
            print(x)
    else:
        print(status)
## vinsamlegst gefið þessu sinn eigin glugga/function

def add_license():
    plane_licenses = None
    continue_input = input("Would you like to add plane licenses? (y/n): ")
    plane_licenses = []
    while continue_input == 'y':
        license_input = input("Enter a plane license: ")
        plane_licenses.append(license_input)
        continue_input = input("Would you like to add another license? (y/n): ")
    return plane_licenses

def modify_employees():
    print("\nModify an Employee's Details")
    employee_id = input("Enter the ID of the employee to modify: ")

    employee = logic_wrapper.get_employee_by_id(employee_id)
    if employee is None:
        print("No employee found with the given ID.")
        return

    print(f"Modifying details for employee {employee.name} (ID: {employee.id})")
    new_details = {
        "cell_phone": input(f"Enter new cell phone number (current: {employee.cell_phone}): ") or employee.cell_phone,
        "email": input(f"Enter new email address (current: {employee.email}): ") or employee.email,
        "home_phone": input(f"Enter new home phone (current: {employee.home_phone}): ") or employee.home_phone,
        "address": input(f"Enter new home address (current: {employee.address}): ") or employee.address,
    }

    if logic_wrapper.is_employee_a_pilot(employee_id):
        add_licenses = input("Would you like to modify plane licenses? (y/n): ")
        if add_licenses.lower() == "y":
            new_details["plane_licenses"] = add_license()

    logic_wrapper.update_employee(employee_id, new_details)
    print("Employee details updated successfully.")
