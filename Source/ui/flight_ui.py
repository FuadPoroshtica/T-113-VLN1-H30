# flight_ui.py

from data.flight_data import Flight_Data
from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper

data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def flights_menu():
    menu_stack.append(flights_menu)
    while True:
        print("\nFlights Menu")
        print("---------------")
        print("1. View Flights")
        print("2. Create New Flight")
        print("3. Modify Flight")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            view_flights() 
        elif choice == '2':
            create_flight()  
        elif choice == '3':
            modify_flight()
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

def view_flights():
    menu_stack.append(view_flights)
    while True:
        all_flights = logic_wrapper.get_all_flights()
        print("\nList of All Flights:")
        print("----------------------")
        for flight in all_flights:
            print(f"{flight.id}: From {flight.initial_location} to {flight.arrival_location}, Plane: {flight.plane}, Start: {flight.start_home}, Tickets: Home - {flight.tickets_home}, Foreign - {flight.tickets_foreign}")

        handle_menu_options()

def create_flight():
    print("\nCreate a New Flight")
    initial_airport_code = input("Enter Initial Airport Code: ")
    arrival_airport_code = input("Enter Arrival Airport Code: ")
    plane_id = input("Enter Plane ID: ")
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    start_time = input("Enter Start Time at Home Location (HH:MM): ")
    tickets_home = input("Enter Number of Home Tickets: ")
    tickets_foreign = input("Enter Number of Foreign Tickets: ")

    employees = []  # Initialize the employees list

    flight_id = logic_wrapper.generate_flight_id(plane_id, arrival_airport_code)
    
    flight_data = {
        'id': flight_id,
        'initial_location': initial_airport_code,
        'arrival_location': arrival_airport_code,
        'initial_location': initial_airport_code,
        'arrival_location': arrival_airport_code,
        'plane': plane_id,
        'start_home': f"{start_date} {start_time}",
        'tickets_home': tickets_home,
        'tickets_foreign': tickets_foreign,
        'employees': employees
    }

    logic_wrapper.add_flight(flight_data)
    print("Flight added successfully.")

def modify_flight():
    print("\nModify Flight Details")
    flight_id = input("Enter the ID of the flight to modify: ")
    flight = logic_wrapper.get_flight_by_id(flight_id)

    if flight is None:
        print("No flight found with the given ID.")
        return

    print(f"Modifying details for Flight {flight.id} (From {flight.initial_location} to {flight.arrival_location})")
    new_details = {
        'initial_location': input(f"Enter new initial location (current: {flight.initial_location}): ") or None,
        'arrival_location': input(f"Enter new arrival location (current: {flight.arrival_location}): ") or None,
        'plane': input(f"Enter new plane ID (current: {flight.plane}): ") or None,
        'start_home': input(f"Enter new start time at home location (current: {flight.start_home}): ") or None,
        'tickets_home': input(f"Enter new number of home tickets (current: {flight.tickets_home}): ") or None,
        'tickets_foreign': input(f"Enter new number of foreign tickets (current: {flight.tickets_foreign}): ") or None
    }

    logic_wrapper.update_flight(flight_id, new_details)
    print("Flight details updated successfully.")