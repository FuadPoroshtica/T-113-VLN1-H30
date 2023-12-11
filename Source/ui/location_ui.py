# location_ui.py
from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper

# Initialize Data_Wrapper and LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def locations_menu():
    menu_stack.append(locations_menu)
    while True:
        print("\nLocations Menu")
        print("---------------")
        print("1. View Locations")
        print("2. Create New Location")
        print("3. Modify Location")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            view_locations() 
        elif choice == '2':
            create_location()  
        elif choice == '3':
            modify_location()
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

def view_locations():
    menu_stack.append(view_locations)
    while True:
        all_locations = logic_wrapper.get_all_locations()
        print("\nList of All Locations:")
        print("----------------------")
        for location in all_locations:
            print(f"{location.id}: {location.country}, {location.airport_code}")

        print("\nMain Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == 'M':
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

def create_location():
    print("\nCreate a New Location")
    id = input("Enter ID: ")
    country = input("Enter Country: ")
    airport_code = input("Enter Airport Code: ")
    flight_duration = input("Enter Flight Duration: ")
    distance = input("Enter Distance: ")
    manager_name = input("Enter Manager Name: ")
    emergency_phone = input("Enter Emergency Phone: ")

    logic_wrapper.add_location(id, country, airport_code, flight_duration, distance, manager_name, emergency_phone)
    print("Location added successfully.")

def modify_location():
    print("\nModify Location Details")
    location_id = input("Enter the ID of the location to modify: ")

    location = logic_wrapper.get_location_by_id(location_id)
    if location is None:
        print("No location found with the given ID.")
        return

    print(f"Modifying details for location {location.country} (ID: {location.id})")
    new_details = {
        'country': input(f"Enter new country (current: {location.country}): ") or None,
        'airport_code': input(f"Enter new airport code (current: {location.airport_code}): ") or None,
        'flight_duration': input(f"Enter new flight duration (current: {location.flight_duration}): ") or None,
        'distance': input(f"Enter new distance (current: {location.distance}): ") or None,
        'manager_name': input(f"Enter new manager name (current: {location.manager_name}): ") or None,
        'emergency_phone': input(f"Enter new emergency phone (current: {location.emergency_phone}): ") or None
    }

    logic_wrapper.update_location_details(location_id, new_details)
    print("Location details updated successfully.")