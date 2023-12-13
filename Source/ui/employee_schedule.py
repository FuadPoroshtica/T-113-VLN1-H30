# employee_schedule_ui.py

from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper

data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def employee_schedule_menu():
    menu_stack.append(employee_schedule_menu)
    while True:
        print("\nEmployee Schedule Menu")
        print("----------------------")
        print("1. Assign Employees to Flight")
        print("2. Modify Flight Employees")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            assign_employees_to_flight()
        elif choice == '2':
            modify_flight_employees()
        elif choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            return_to_previous_menu()
            break
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

def assign_employees_to_flight():
    flight_id = input("Enter the Flight ID to assign employees to: ")
    flight = logic_wrapper.get_flight_by_id(flight_id)

    if flight:
        print("Assigning employees to flight:", flight_id)
        assign_pilots(flight_id)
        assign_stewards(flight_id)
        print("Employees assigned successfully.")
    else:
        print("No flight found with the given ID.")

def assign_pilots(flight_id):
    pilots = logic_wrapper.get_pilots()
    print("\nAvailable Pilots:")
    for pilot in pilots:
        print(f"{pilot.id}: {pilot.name}")

    selected_pilots = input("Enter Pilot IDs (comma-separated, choose 2): ").split(',')
    logic_wrapper.assign_employees_to_flight(flight_id, selected_pilots)

def assign_stewards(flight_id):
    stewards = logic_wrapper.get_cabin_crew()
    print("\nAvailable Stewards:")
    for steward in stewards:
        print(f"{steward.id}: {steward.name}")

    selected_stewards = input("Enter Steward IDs (comma-separated, at least 1): ").split(',')
    logic_wrapper.assign_employees_to_flight(flight_id, selected_stewards)


def modify_flight_employees():
    flight_id = input("Enter the Flight ID to modify employees: ")
    flight = logic_wrapper.get_flight_by_id(flight_id)

    if flight:
        print(f"Current employees on flight {flight_id}: {', '.join(flight.employees)}")
        print("Enter new employee IDs to assign to this flight.")

        logic_wrapper.clear_flight_employees(flight_id)

        # Assign new pilots and stewards
        assign_pilots(flight_id)
        assign_stewards(flight_id)

        print("Employees updated successfully for the flight.")
    else:
        print("No flight found with the given ID.")
