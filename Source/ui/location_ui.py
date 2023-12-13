# location_ui.py

from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from ui.interface_ui import print_boxed

# Initialize Data_Wrapper and LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def locations_menu():
    menu_stack.append(locations_menu)
    while True:
        content = [
            "Locations Menu",
            "---------------",
            "1. View Locations",
            "2. Create New Location",
            "3. Modify Location",
            "Main Menu (M), Back (B), Quit (Q)"
        ]

        choice = print_boxed(content)

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
        content = [
            "List of All Locations:",
            "----------------------",
            *["{}: {}, {}".format(location.id, location.country, location.airport_code) for location in all_locations],
            "Main Menu (M), Back (B), Quit (Q)"
        ]
        choice = print_boxed(content)
        handle_menu_options()

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
    new_details = { #Only things allowed to change
        'manager_name': input(f"Enter new manager name (current: {location.manager_name}): ") or None,
        'emergency_phone': input(f"Enter new emergency phone (current: {location.emergency_phone}): ") or None
    }

    logic_wrapper.update_location_details(location_id, new_details)
    print("Location details updated successfully.")