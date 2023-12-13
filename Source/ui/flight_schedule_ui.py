# location_ui.py

from .navigation import return_to_previous_menu, return_to_main_menu, handle_menu_options, menu_stack
from logic.logic_wrapper import Logic_Wrapper
from data.data_wrapper import Data_Wrapper

# Initialize Data_Wrapper and LogicWrapper
data_wrapper = Data_Wrapper()
logic_wrapper = Logic_Wrapper(data_wrapper)


def flight_schedule_menu():
    menu_stack.append(flight_schedule_menu)
    while True:
        print("Flight Schedule Menu")
        print("--------------------")

        print("1. View Todays flights")
        print("2. View This weeks flights")
        print("3. View specific days flights")
        print("4. View specific weeks flights")
        print("5. Create new flight")

        print("Main Menu (M), Back (B), Quit (Q)")
        choice = input("Select Option: ").upper()

        if choice == '1':
            get_daily_flights()
        elif choice == '2':
            get_weekly_flight()
        elif choice == '3':
            search_for_flight()
        elif choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            return_to_main_menu()
            break
        elif choice == 'Q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

def get_daily_flights():
    menu_stack.append(get_daily_flights)
    while True:
        daily_flights = logic_wrapper.get_day_flights()
        print("\nList of Todays flights:")
        print("----------------------")
        for flight in daily_flights:
            print(f"{flight.id}")