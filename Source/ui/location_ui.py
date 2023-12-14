# location_ui.py
import time

from model.location_model import Location
from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper

from ui.interface_ui import interface

#from ui.ascii_ui import location_added_success

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

        interface(content)
        choice = input("Select option: ").upper()

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
            *["{}: {}, {}, {}, {}".format(location.id, location.country, location.airport_code, location.manager_name, f"+{location.emergency_phone}") for location in all_locations],
            "Main Menu (M), Back (B), Quit (Q)"
        ]

        interface(content)
        handle_menu_options()

def create_location():
    print("Create New Location")
    prompts = [
        "Enter ID",
        "Enter Country",
        "Enter Airport Code",
        "Enter Flight Duration",
        "Enter Distance",
        "Enter Manager Name",
        "Enter Emergency Phone"
    ]

    # Store inputs in a dictionary
    inputs = {}
    for prompt in prompts:
        interface([prompt])  # Display each prompt using the interface function
        inputs[prompt] = input("Type here: ").strip()

    # Prepare the location data
    location_data = Location(
        inputs["Enter ID"],
        inputs["Enter Country"],
        inputs["Enter Airport Code"],
        inputs["Enter Flight Duration"],
        inputs["Enter Distance"],
        inputs["Enter Manager Name"],
        inputs["Enter Emergency Phone"]
    )

    # Add the location using logic_wrapper
    logic_wrapper.add_location(location_data)


    interface(["Location added successfully."])

    time.sleep(2)

    # Return to the previous menu
    return return_to_previous_menu()


def modify_location():
    print("\nModify Location Details")
    location_id = input("Enter the ID of the location to modify: ")

    location = logic_wrapper.get_location_by_id(location_id)
    if location is None:
        print("No location found with the given ID.")
        return

    print(f"Modifying details for employee {location.manager_name} (ID: {location.id})")
    new_details = {
        "manager": input(f"Enter new manager (current: {location.manager_name}): ") or location.manager_name,
        "cell_phone": input(f"Enter new emergency phone number (current: {location.emergency_phone}): ") or location.emergency_phone
    }

    logic_wrapper.update_location(location_id, new_details)
    print("Location details updated successfully.")

