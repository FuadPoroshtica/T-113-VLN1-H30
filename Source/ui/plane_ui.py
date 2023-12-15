#plane_ui.py
import time
from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack, handle_menu_options 
from datetime import datetime, timedelta
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from model.plane_model import Plane
from ui.interface_ui import interface


# Initialize LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def planes_menu():
    menu_stack.append(planes_menu)
    while True:
        content = [
            "Planes Menu",
            "------------------------------",
            "1. View Planes",
            "2. Create New Plane",
            "3. Modify Plane",
            "4. View Plane Licenses",
            "5. Search Pilots by Plane Type",
            "6. Check Plane Status by Time",
            "7. View Upcoming Flights for a Plane",
            "------------------------------",
            "Main Menu (M), Back (B), Quit (Q)"
        ]

        interface(content)
        choice = input("Select option: ").upper()

        if choice == '1':
            view_planes() 
        elif choice == '2':
            create_plane()  
        elif choice == '3':
            modify_plane()
        elif choice == '4':
            view_plane_licenses()
        elif choice == '5':
            search_pilots_by_plane_type()
        elif choice == '6':
            check_plane_status()
        elif choice == '7':
            view_upcoming_flights_for_plane()
        
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


def view_planes():
    menu_stack.append(view_planes)
    all_planes = logic_wrapper.get_all_planes()

    # Using list comprehension to format plane details
    content = [
        "List of All Planes:",
        "-------------------",
        *["ID: {}, Airline: {}, Model: {}, Capacity: {}".format(plane.id, plane.airline_name, plane.airplane_model,
                                                                plane.max_capacity) for plane in all_planes],
        "Main Menu (M), Back (B), Quit (Q)"
    ]

    interface(content)
    handle_menu_options()

def create_plane():
    print("Create a New Plane")
    prompts = [
        "Enter ID",
        "Enter Airline Name",
        "Enter Airplane Mode",
        "Enter Max Capacity"
    ]

    # Store inputs in a dictionary
    inputs = {}
    for prompt in prompts:
        interface([prompt])  # Display each prompt using the interface function
        inputs[prompt] = input("Type here: ").strip()

    # Prepare the plane data
    new_plane = Plane(
        inputs["Enter ID"],
        inputs["Enter Airline Name"],
        inputs["Enter Airplane Mode"],
        inputs["Enter Max Capacity"]
    )

    # Add the location using logic_wrapper
    logic_wrapper.add_plane(new_plane)


    interface(["Plane added successfully."])

    time.sleep(2)

    # Return to the previous menu
    return planes_menu()


def modify_plane():
    menu_stack.append(modify_plane)

    interface(["Enter the ID of the plane to modify"])
    plane_id = input("Type here: ").strip()
    plane = logic_wrapper.get_plane_by_id(plane_id)

    if plane is None:
        interface(["No plane found with the given ID."])
        time.sleep(2)
        return

    content = [f"Modifying details for plane {plane.airplane_model} (ID: {plane.id})"]
    interface(content)

    new_details = {
        'airline_name': input(f"Enter new airline name (current: {plane.airline_name}): ") or plane.airline_name,
        'airplane_model': input(
            f"Enter new airplane model (current: {plane.airplane_model}): ") or plane.airplane_model,
        'max_capacity': input(f"Enter new max capacity (current: {plane.max_capacity}): ") or plane.max_capacity
    }

    logic_wrapper.update_plane(plane_id, new_details)

    interface(["Plane details updated successfully."])
    time.sleep(2)

    # Return to the previous menu
    return planes_menu()

def view_plane_licenses():
    menu_stack.append(view_plane_licenses)
    all_planes = logic_wrapper.get_all_planes()  
    licenses = logic_wrapper.get_all_plane_licenses()  

    fleet_models = set(plane.airplane_model for plane in all_planes)

    fleet_licenses = {model: [] for model in fleet_models} 
    non_fleet_licenses = {}

    for model, pilots in licenses.items():
        if model in fleet_models:
            fleet_licenses[model] = pilots
        else:
            non_fleet_licenses[model] = pilots

    content = ["Plane License Information:",
               "--------------------------",
               "In Current Fleet:"]

    for model in fleet_models:
        content.append(f"{model} License Holders:")
        if fleet_licenses[model]:
            for id, name in fleet_licenses[model]:
                content.append(f"  Pilot ID: {id}, Name: {name}")
        else:
            content.append("  No licensed pilots for this plane model.")

    content.append("Not in Current Fleet:")
    for model, pilots in non_fleet_licenses.items():
        content.append(f"{model} License Holders:")
        for id, name in pilots:
            content.append(f"  Pilot ID: {id}, Name: {name}")

    interface(content)
    handle_menu_options()

def search_pilots_by_plane_type():
    menu_stack.append(search_pilots_by_plane_type)
    interface(["Enter plane type (e.g., Boeing 747): "])
    plane_type = input("Type here: ").strip()

    pilots = logic_wrapper.get_pilots_by_plane_type(plane_type)
    content = [f"\nPilots licensed to fly {plane_type}:"]
    if pilots:
        for pilot in pilots:
            content.append(f"ID: {pilot.id}, Name: {pilot.name}")
    else:
        content.append("No pilots found with a license to fly this plane type.")

    interface(content)
    handle_menu_options()

def check_plane_status():
    menu_stack.append(check_plane_status)
    interface(["Enter the date and time (YYYY-MM-DD HH:MM): "])
    input_time_str = input("Type here: ").strip()

    try:
        input_time = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M")
        plane_statuses = logic_wrapper.get_plane_statuses_at_time(input_time)
        content = [str(status) for status in plane_statuses]
    except ValueError as e:
        content = ["Error: Invalid date/time format. Please use YYYY-MM-DD HH:MM format.", str(e)]

    interface(content)
    handle_menu_options()

def view_upcoming_flights_for_plane():
    menu_stack.append(view_upcoming_flights_for_plane)
    interface(["Enter the Plane ID: "])
    plane_id = input("Type here: ").strip()

    upcoming_flights = logic_wrapper.get_upcoming_flights_for_plane(plane_id)
    content = [f"\nUpcoming flights for Plane ID {plane_id}:"]
    if upcoming_flights:
        for flight in upcoming_flights:
            content.append(f"Flight ID: {flight.id}, To: {flight.arrival_location}, Departure: {flight.start_home}")
    else:
        content.append("No upcoming flights found for this Plane ID.")

    interface(content)
    handle_menu_options()