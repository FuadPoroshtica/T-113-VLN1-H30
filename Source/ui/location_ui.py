# location_ui.py

from model.location_model import Location
from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from ui.interface_ui import print_boxed, print_boxed_with_inputs, print_boxed_with_inputs_modify

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
    # Define the input prompts
    prompts = [
        "Enter ID",
        "Enter Country",
        "Enter Airport Code",
        "Enter Flight Duration",
        "Enter Distance",
        "Enter Manager Name",
        "Enter Emergency Phone"
    ]

    # Use the modified print_boxed function to get inputs
    inputs = print_boxed_with_inputs(prompts)

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
    
    # Confirmation message
    print("Location added successfully.")


def modify_location():
    location_id = input("Enter the ID of the location to modify: ")  # This initial input remains outside the box

    location = logic_wrapper.get_location_by_id(location_id)
    if location is None:
        print("No location found with the given ID.")
        return

    # Static information to display
    info_lines = [
        "Modify Location Details",
        f"Modifying details for location {location.country} (ID: {location.id})"
    ]
    
    # Input prompts
    input_prompts = [
        f"Enter new manager name (current: {location.manager_name})",
        f"Enter new emergency phone (current: {location.emergency_phone})"
    ]

    # Use the modified print_boxed function to get inputs
    new_details = print_boxed_with_inputs_modify(info_lines, input_prompts)

    # Prepare the details to be updated
    update_details = {
        'manager_name': new_details.get(input_prompts[0]),
        'emergency_phone': new_details.get(input_prompts[1])
    }

    # Filtering out None values if no new input was provided
    update_details = {k: v for k, v in update_details.items() if v is not None}

    logic_wrapper.update_location_details(location_id, update_details)
    print("Location details updated successfully.")
