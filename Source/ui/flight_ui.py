# flight_ui.py

from datetime import datetime, timedelta
from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from ui.interface_ui import interface

data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def flights_menu():
    menu_stack.append(flights_menu)
    while True:
        content = [
            "Flights Menu",
            "---------------------------------------------",
            "1. View Flights",
            "2. Create New Flight",
            "3. View Flights by Date",
            "4. View Flights by Week",
            "---------------------------------------------",
            "Main Menu (M), Back (B), Quit (Q)",
        ]
        interface(content)
        choice = input("Select Option: ").upper()

        if choice == '1':
            view_flights()
        elif choice == '2':
            create_flight()
        elif choice == '3':
            view_flights_by_date()
        elif choice == '4':
            view_flights_by_week()
        elif choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            return_to_previous_menu()
            break
        elif choice == 'Q':
            interface(["Exiting the program."])
            exit()
        else:
            interface(["Invalid choice. Please choose again."])


def view_flights():
    menu_stack.append(view_flights)
    while True:
        all_flights = logic_wrapper.get_all_flights()

        # Building the content list for interface
        flights_content = ["List of All Flights:", "----------------------"]
        if all_flights:
            flights_content.extend(
                [
                    f"{flight.id}: From {flight.initial_location} to {flight.arrival_location}, Plane: {flight.plane}, Start: {flight.start_home}, Tickets: Home - {flight.tickets_home}, Foreign - {flight.tickets_foreign}"
                    for flight in all_flights]
            )
        else:
            flights_content.append("No flights available.")

        interface(flights_content)
        handle_menu_options()


def input_with_retry(prompt, validation_func):
    while True:
        input_value = input(prompt)
        if validation_func(input_value):
            return input_value
        retry = input("Error, input not valid. Would you like to try again? (y/n): ").lower()
        if retry == 'n':
            return "exit"

def input_ticket_count(prompt, max_capacity):
    while True:
        print([prompt])
        input_str = input("Type here: ")

        if not input_str.isdigit():
            interface(["Invalid input, please enter a valid integer number."])
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry == 'n':
                return "exit"  # Return a special value to indicate exit
            continue

        tickets = int(input_str)
        if tickets > max_capacity:
            interface([f"Error: Ticket count exceeds the maximum seat capacity of {max_capacity}."])
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry == 'n':
                return "exit"
        else:
            return tickets


def create_flight():
    interface(["Create a New Flight"])

    initial_airport_code = input_with_retry("Enter Initial Airport Code: ",
                                            lambda code: logic_wrapper.location_logic.get_location_by_airport_code(
                                                code))
    if initial_airport_code == "exit":
        return

    arrival_airport_code = input_with_retry("Enter Arrival Airport Code: ",
                                            lambda code: logic_wrapper.location_logic.get_location_by_airport_code(
                                                code))
    if arrival_airport_code == "exit":
        return

    plane_id = input_with_retry("Enter Plane ID: ", lambda pid: logic_wrapper.plane_logic.get_plane_by_id(pid))
    if plane_id == "exit":
        return

    print("Enter Start Date (YYYY-MM-DD):")
    start_date = input("Type here: ")
    print("Enter Start Time at Home Location (HH:MM):")
    start_time = input("Type here: ")
    start_home = f"{start_date} {start_time}"

    plane = logic_wrapper.plane_logic.get_plane_by_id(plane_id)
    max_capacity = int(plane.max_capacity) if plane else 0
    tickets_home = input_ticket_count("Enter Number of Home Tickets: ", max_capacity)
    if tickets_home == "exit":
        return

    tickets_foreign = input_ticket_count("Enter Number of Foreign Tickets: ", max_capacity)
    if tickets_foreign == "exit":
        return

    valid, message = logic_wrapper.validate_flight_creation(plane_id, start_home, arrival_airport_code, tickets_home,
                                                            tickets_foreign)
    if not valid:
        interface([f"Error: {message}"])
        return

    flight_id = logic_wrapper.flight_logic.generate_flight_id(plane, arrival_airport_code, start_home)

    flight_data = {
        'id': flight_id,
        'initial_location': initial_airport_code,
        'arrival_location': arrival_airport_code,
        'plane': plane_id,
        'start_home': start_home,
        'tickets_home': tickets_home,
        'tickets_foreign': tickets_foreign,
        'employees': []
    }

    logic_wrapper.add_flight(flight_data)
    interface(["Flight added successfully."])


def view_flights_by_date():
    interface(["Enter Date (YYYY-MM-DD): "])
    start_date = input("Type here: ").strip()

    if not start_date:
        return flights_menu()

    flights = logic_wrapper.get_flights_by_week_with_manning_info(start_date)

    flight_content = ["Flights for the week starting from " + start_date]
    for flight, is_manned in flights:
        flight_content.append(
            f"Flight {flight.id} on {flight.start_home}: {'Properly Manned' if is_manned else 'Not Properly Manned'}")

    flight_content.append("\nPress Enter to return to the Flights Menu.")
    interface(flight_content)

    input()
    return flights_menu()


def view_flights_by_week():
    interface(["Enter Start Date of Week (YYYY-MM-DD):"])
    start_date = input("Type here: ").strip()
    flights = logic_wrapper.get_flights_by_week_with_manning_info(start_date)

    flight_content = ["Flights for the week starting from " + start_date]
    for flight, is_manned in flights:
        flight_content.append(f"Flight {flight.id} on {flight.start_home}: {'Properly Manned' if is_manned else 'Not Properly Manned'}")

    interface(flight_content)

    input()
    return flights_menu()

