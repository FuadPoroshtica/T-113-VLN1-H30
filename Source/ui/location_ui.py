# location_ui.py

from model.location_model import Location
from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from ui.interface_ui import interface, print_boxed_with_inputs

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
            *["{}: {}, {}".format(location.id, location.country, location.airport_code) for location in all_locations],
            "Main Menu (M), Back (B), Quit (Q)"
        ]

        interface(content)
        choice = input("Select option: ").upper()
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

    # Confirmation message
    print("Location added successfully.")



def create_update_details(new_details, detail_keys):
    update_details = {key: new_details.get(key) for key in detail_keys}
    update_details = {k: v for k, v in update_details.items() if v is not None}
    return update_details


def modify_location():
    location_id = input("Enter the ID of the location to modify: ")
    location = logic_wrapper.get_location_by_id(location_id)

    if location is None:
        print("No location found with the given ID.")
        return

    info_lines = [
        "Modify Location Details",
        f"Modifying details for location {location.country} (ID: {location.id})"
    ]
    manager_prompt = f"Enter new manager name (current: {location.manager_name})"
    phone_prompt = f"Enter new emergency phone (current: {location.emergency_phone})"
    input_prompts = [manager_prompt, phone_prompt]

    inputs = interface(info_lines, input_prompts)

    new_details = inputs
    detail_keys = [manager_prompt, phone_prompt]
    update_details = create_update_details(new_details, detail_keys)
    logic_wrapper.update_location_details(location_id, update_details)
    print("Location details updated successfully.")