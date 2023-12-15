#employee_schedule.py

from datetime import datetime
from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from ui.location_ui import interface

data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def employee_schedule_menu():
    menu_stack.append(employee_schedule_menu)
    while True:
        print("\nEmployee Schedule Menu")
        print("------------------------")
        print("1. Add Employees to Flights")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            add_employees_to_flight()
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

def add_employees_to_flight():
    undermanned_flights = logic_wrapper.get_undermanned_flights()
    if not undermanned_flights:
        print("\nNo undermanned flights found.")
        return

    print("\nUndermanned Flights:")
    for flight in undermanned_flights:
        print(f"{flight.id}: From {flight.initial_location} to {flight.arrival_location}")

    flight_id = input("\nEnter Flight ID to add employees: ")
    selected_flight = logic_wrapper.get_flight_by_id(flight_id)

    if not selected_flight:
        print("Flight not found.")
        return

    available_pilots = logic_wrapper.get_available_pilots_for_flight(flight_id)
    print("\nAvailable Pilots:")
    for pilot in available_pilots:
        print(f"{pilot.id}: {pilot.name}")

    while True:
        pilot_id = input("Enter Pilot ID to add (or 'done' to finish): ")
        if pilot_id.lower() == 'done':
            break
        if logic_wrapper.add_pilot_to_flight(flight_id, pilot_id):
            print("Pilot added successfully.")
        else:
            print("Invalid Pilot ID or Pilot not available.")

    available_stewards = logic_wrapper.get_available_stewards_for_flight(flight_id)
    print("\nAvailable Stewards:")
    for steward in available_stewards:
        print(f"{steward.id}: {steward.name}")

    while True:
        steward_id = input("Enter Steward ID to add (or 'done' to finish): ")
        if steward_id.lower() == 'done':
            break
        if logic_wrapper.add_steward_to_flight(flight_id, steward_id):
            print("Steward added successfully.")
        else:
            print("Invalid Steward ID or Steward not available.")
