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
        content = [
            "Employee Schedule Menu",
            "------------------------------------------------",
            "1. Add Employees to Flights",
            "------------------------------------------------",
            "Main Menu (M), Back (B), Quit (Q)",
        ]
        interface(content)
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
            interface(["Exiting the program."])
            exit()
        else:
            interface(["Invalid choice. Please choose again."])


def add_employees_to_flight():
    undermanned_flights = logic_wrapper.get_undermanned_flights()
    if not undermanned_flights:
        interface(["No undermanned flights found."])
        return

    flights_content = ["Undermanned Flights:"] + \
                      [f"{flight.id}: From {flight.initial_location} to {flight.arrival_location}" for flight in undermanned_flights]
    interface(flights_content)

    interface(["Enter Flight ID to add employees:"])
    flight_id = input("Type here: ").strip()
    selected_flight = logic_wrapper.get_flight_by_id(flight_id)

    if not selected_flight:
        interface(["Flight not found."])
        return

    available_pilots = logic_wrapper.get_available_pilots_for_flight(flight_id)
    pilots_content = ["Available Pilots:"] + \
                     [f"{pilot.id}: {pilot.name}" for pilot in available_pilots]
    interface(pilots_content)

    while True:
        interface(["Enter Pilot ID to add (or 'done' to finish):"])
        pilot_id = input("Type here: ").strip().lower()
        if pilot_id == 'done':
            break
        if logic_wrapper.add_pilot_to_flight(flight_id, pilot_id):
            interface(["Pilot added successfully."])
        else:
            interface(["Invalid Pilot ID or Pilot not available."])

    available_stewards = logic_wrapper.get_available_stewards_for_flight(flight_id)
    stewards_content = ["Available Stewards:"] + \
                       [f"{steward.id}: {steward.name}" for steward in available_stewards]
    interface(stewards_content)

    while True:
        interface(["Enter Steward ID to add (or 'done' to finish):"])
        steward_id = input("Type here: ").strip().lower()
        if steward_id == 'done':
            break
        if logic_wrapper.add_steward_to_flight(flight_id, steward_id):
            interface(["Steward added successfully."])
        else:
            interface(["Invalid Steward ID or Steward not available."])

