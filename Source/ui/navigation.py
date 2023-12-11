# navigation.py
menu_stack = []

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

