#plane_ui.py

from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack, handle_menu_options 
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper
from model.plane_model import Plane

# Initialize LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)

def planes_menu():
    menu_stack.append(planes_menu)
    while True:
        print("\nPlanes Menu")
        print("-----------")
        print("1. View Planes")
        print("2. Create New Plane")
        print("3. Modify Plane")
        print("4. View Plane Licenses")
        print("5. Search Pilots by Plane Type")
        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

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
    print("\nList of All Planes:")
    print("-------------------")
    for plane in all_planes:
        print(f"ID: {plane.id}, Airline: {plane.airline_name}, Model: {plane.airplane_model}, Capacity: {plane.max_capacity}")
    
    handle_menu_options()
    
def create_plane():
    print("\nCreate a New Plane")
    id = input("Enter ID: ")
    airline_name = input("Enter Airline Name: ")
    airplane_model = input("Enter Airplane Model: ")
    max_capacity = input("Enter Max Capacity: ")

    new_plane = Plane(id, airline_name, airplane_model, max_capacity)
    logic_wrapper.add_plane(new_plane)
    print("Plane added successfully.")

def modify_plane():
    plane_id = input("Enter the ID of the plane to modify: ")

    plane = logic_wrapper.get_plane_by_id(plane_id)
    if plane is None:
        print("No plane found with the given ID.")
        return

    print(f"Modifying details for plane {plane.airplane_model} (ID: {plane.id})")
    new_details = {
        'airline_name': input(f"Enter new airline name (current: {plane.airline_name}): ") or None,
        'airplane_model': input(f"Enter new airplane model (current: {plane.airplane_model}): ") or None,
        'max_capacity': input(f"Enter new max capacity (current: {plane.max_capacity}): ") or None
    }

    logic_wrapper.update_plane(plane_id, new_details)
    print("Plane details updated successfully.")

def view_plane_licenses():
    menu_stack.append(view_plane_licenses)
    licenses = logic_wrapper.get_all_plane_licenses()
    if not licenses:
        print("No plane license information available.")
        return
    print("\nPlane License Information:")
    print("--------------------------")
    for plane_type, employees in licenses.items():
        print(f"\n{plane_type} License Holders:")
        for id, name in employees:
            print(f"ID: {id}, Name: {name}")

    handle_menu_options()

def search_pilots_by_plane_type():
    menu_stack.append(search_pilots_by_plane_type)
    plane_type = input("Enter plane type (e.g., Boeing 747): ")
    pilots = logic_wrapper.get_pilots_by_plane_type(plane_type)
    if pilots:
        print(f"\nPilots licensed to fly {plane_type}:")
        for pilot in pilots:
            print(f"ID: {pilot.id}, Name: {pilot.name}")
    else:
        print(f"No pilots found with a license to fly {plane_type}.")

    handle_menu_options()