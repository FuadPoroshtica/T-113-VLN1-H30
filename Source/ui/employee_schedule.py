#employee_schedule.py

from datetime import datetime, timedelta
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
            "2. View Employee Schedule for a Week",
            "------------------------------------------------",
            "3. Show Employees Working Status on a Specific Day",
            "------------------------------------------------",

            "Main Menu (M), Back (B), Quit (Q)",
        ]
        interface(content)
        choice = input("Select Option: ").upper()

        if choice == '1':
            add_employees_to_flight()
        elif choice == '2':
            view_employee_schedule()
        elif choice == '3':
            show_employee_working_status()
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

def view_employee_schedule():
    employee_id = input("Enter Employee ID: ")
    employee = logic_wrapper.get_employee_by_id(employee_id)

    if not employee:
        print("Employee ID does not exist.")
        return

    date_input = input("Enter a specific date (YYYY-MM-DD) to check the schedule: ")
    try:
        specific_date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    start_of_week = specific_date - timedelta(days=specific_date.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday

    print(f"\nSchedule for {employee.name} from {start_of_week.date()} to {end_of_week.date()}:")
    flights = logic_wrapper.get_all_flights()
    for flight in flights:
        if employee_id in flight.employees:
            flight_date = datetime.strptime(flight.start_home, "%Y-%m-%d %H:%M").date()
            if start_of_week.date() <= flight_date <= end_of_week.date():
                print(f"- Flight {flight.id}: From {flight.initial_location} to {flight.arrival_location} on {flight.start_home}")

def show_employee_working_status():
    specific_date_input = input("Enter the specific date (YYYY-MM-DD) to check: ")
    try:
        specific_date = datetime.strptime(specific_date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    all_employees = logic_wrapper.get_all_employees()
    all_flights = logic_wrapper.get_all_flights()

    working_employees = []
    not_working_employees = {employee.id: employee for employee in all_employees}

    for flight in all_flights:
        flight_date = datetime.strptime(flight.start_home, "%Y-%m-%d %H:%M").date()
        if flight_date == specific_date:
            for employee_id in flight.employees:
                if employee_id in not_working_employees:
                    employee = not_working_employees.pop(employee_id)
                    working_employees.append((employee, flight))

    print("\nEmployees working on " + specific_date_input + ":")
    for employee, flight in working_employees:
        print(f"{employee.name} (ID: {employee.id}) - Flight {flight.id} from {flight.initial_location} to {flight.arrival_location}")

    print("\nEmployees not working on " + specific_date_input + ":")
    for employee_id, employee in not_working_employees.items():
        print(f"{employee.name} (ID: {employee.id})")