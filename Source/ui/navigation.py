# navigation.py
menu_stack = []
from ui.interface_ui import interface
def return_to_previous_menu():
    if len(menu_stack) > 1:
        menu_stack.pop()  
        previous_menu = menu_stack.pop()  
        previous_menu()  
    else:
        print("No previous menu available.")

def return_to_main_menu():
    global menu_stack
    while len(menu_stack) > 1:
        menu_stack.pop()
    if menu_stack:
        main_menu_func = menu_stack.pop()
        main_menu_func()

def handle_menu_options():
    print("\nMain Menu (M), Back (B), Quit (Q)")
    while True:
        choice = input("Select Option: ").upper()

        if choice == 'M':
            return_to_main_menu()
            break
        elif choice == 'B':
            return_to_previous_menu()
            break
        elif choice == 'Q':
            interface(print("Exiting the program."))
            exit()
        else:
            print("Invalid choice. Please choose again.")


