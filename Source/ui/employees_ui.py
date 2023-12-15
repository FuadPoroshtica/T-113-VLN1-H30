# employees_ui.py
from model.employee_model import Employee
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from ui.interface_ui import interface
from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack, handle_menu_options

import time
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
        "List of All Employees",
        "----------------------",
        "",
        #*["ID: {:<10}, Name: {:<20}, Title: {:<15}, Address: {:<25}, Cell: {:<15}, Email: {:<25}, Home Phone: {:<15}, Current Trip: {:<15}, Lincenses: {} ".format(employee.id, employee.name, employee.title, employee.address, employee.cell_phone, employee.email, employee.home_phone, employee.current_trip, employee.plane_licenses) for employee in all_employees]
        '---------------------------------------------------',
        '|ID         |Name                 |Title          |',
        '---------------------------------------------------',
        *["|{:<10},|{:<20},|{:<15}|".format(employee.id, employee.name, employee.title) for employee in all_employees],
        '---------------------------------------------------',
        'Type 1 to search for pecific employee'
    ]

    interface(content)

    while True:
        choice = input("Select option: ").upper()
        if choice == '1':
            view_employee()
        elif choice == 'M':
            return_to_main_menu()
        elif choice == 'B':
            return_to_previous_menu()
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")
def view_employee():
    menu_stack.append(view_employee)

    # Fetching all employees
    all_employees = logic_wrapper.get_all_employees()
    if not all_employees:
        interface(["No employees found."])
        time.sleep(2)
        return view_all_employees()

    # Displaying a list of all employees with IDs
    employee_list_content = [
        '---------------------------------------------------',
        "The Employee:",
        *["ID: {:<10}, Name: {:<20}".format(employee.id, employee.name) for employee in all_employees],
        '---------------------------------------------------',
        "Enter the ID of the employee to view details, or type 'back' to return:"
    ]
    interface(employee_list_content)

    # Input for selecting an employee
    selected_id = input("Type here: ").strip()
    if selected_id.lower() == 'back':
        return handle_menu_options()

    # Fetch and display details of the selected employee
    selected_employee = logic_wrapper.get_employee_by_id(selected_id)
    if selected_employee:
        employee_details_content = [
            '---------------------------------------------------',
            f"Details for employee ID {selected_id}:",
            f"Name: {selected_employee.name}",
            f"Title: {selected_employee.title}",
            f"Address: {selected_employee.address}",
            f"Cell Phone: {selected_employee.cell_phone}",
            f"Email: {selected_employee.email}",
            f"Home Phone: {selected_employee.home_phone}",
            f"Current Trip: {selected_employee.current_trip}",
            f"Plane Licenses: {', '.join(selected_employee.plane_licenses)}",
            '---------------------------------------------------',
        ]
        interface(employee_details_content)
    else:
        interface([f"No employee found with ID {selected_id}."])
        time.sleep(2)
    return view_all_employees()


def add_employees():
    print("Adding new employees...")
    prompts = [
        'Enter ID',
        'Enter Name',
        'Enter Home Address',
        'Enter Cell Phone',
        'Enter Email'
    ]

    # Store inputs in a dictionary
    inputs = {}
    for prompt in prompts:
        interface([prompt])  # Display each prompt using the interface function
        inputs[prompt] = input("Type here: ").strip()

    # Ask for title
    interface(['Enter Title (Pilot/Cabin Crew)'])
    title = input("Type here: ").strip().lower()
    inputs['Enter Title'] = title

    plane_licenses = "None"
    if title == "pilot":
        plane_licenses = add_license()  # Ensure add_license() is defined

    # Enter optional home phone
    interface(['Enter Home Phone (Optional)'])
    inputs['Enter Home Phone (Optional)'] = input("Type here: ").strip()

    # Prepare the employee data
    new_employee = Employee(
        inputs['Enter ID'],
        inputs['Enter Name'],
        inputs['Enter Home Address'],
        inputs['Enter Cell Phone'],
        inputs['Enter Email'],
        title,
        inputs.get('Enter Home Phone (Optional)', ''),
        plane_licenses
    )

    status = logic_wrapper.add_employee(new_employee)

    # Interface to display the status or errors
    if isinstance(status, list):  # Checks if status is a list of errors
        content = [""]
        content.extend(status)
    else:
        content = [status, "Employee added successfully."]

    interface(content)

    time.sleep(4)
    return employees_menu()

def add_license():
    plane_licenses = []
    continue_input = input("Would you like to add plane licenses? (y/n): ")
    while continue_input.lower() == 'y':
        license_input = input("Enter a plane license: ")
        plane_licenses.append(license_input)
        continue_input = input("Would you like to add another license? (y/n): ")
    return plane_licenses


def modify_employees():
    menu_stack.append(modify_employees)

    interface(["Enter the ID of the employee to modify"])
    employee_id = input("Type here: ").strip()
    employee = logic_wrapper.get_employee_by_id(employee_id)

    if employee is None:
        interface(["No employee found with the given ID."])
        time.sleep(2)
        return

    content = [f"Modifying details for employee {employee.name} (ID: {employee.id})"]
    interface(content)

    new_details = {
        'cell_phone': input(f"Enter new cell phone number (current: {employee.cell_phone}): ") or employee.cell_phone,
        'email': input(f"Enter new email address (current: {employee.email}): ") or employee.email,
        'home_phone': input(f"Enter new home phone (current: {employee.home_phone}): ") or employee.home_phone,
        'address': input(f"Enter new home address (current: {employee.address}): ") or employee.address
    }

    if logic_wrapper.is_employee_a_pilot(employee_id):
        add_licenses = input("Would you like to modify plane licenses? (y/n): ")
        if add_licenses.lower() == 'y':
            new_details['plane_licenses'] = add_license()  # Ensure add_license() is defined

    logic_wrapper.update_employee(employee_id, new_details)

    interface(["Employee details updated successfully."])
    time.sleep(2)

    return employees_menu()  # Ensure this function is defined
