import os
# main_menu_ui.py

from ui.employee_schedule import employee_schedule_menu
from ui.plane_ui import planes_menu
from ui.location_ui import locations_menu
from ui.flight_ui import flights_menu
from ui.employees_ui import employees_menu
from ui.interface_ui import print_boxed
from .navigation import return_to_previous_menu, return_to_main_menu, menu_stack



# Inside your login_screen and main_menu functions
def login_screen():
    while True:
        content = [
            "Login Screen",
            "------------",
            "Login (press L)",
            "Quit (press Q)"
        ]
        choice = print_boxed(content)

        if choice == 'L':
            main_menu()
        elif choice == 'Q':
            exit()
        else:
            print("Invalid choice. Please choose again.")


def main_menu():
    menu_stack.append(main_menu)
    while True:
        content = [
            "Main Menu",
            "-----------",
            "1. Locations",
            "2. Flight crew",
            "3. Planes",
            "4. Flights",
            "5. Employees",
            "6. Logout",
            "Q. Quit"
        ]

        choice = print_boxed(content)

        if choice == '1':
            locations_menu()
        elif choice == '2':
            employee_schedule_menu()
        elif choice == '3':
            planes_menu()
        elif choice == '4':
            flights_menu()
        elif choice == '5':
            employees_menu()
        elif choice == '6':
            login_screen()
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

def interface(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = 10/i if i != 0 else "Undefined" # Avoid division by zero
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(i, v))

    stdscr.refresh()
    stdscr.getkey()
