import os

def print_boxed(text_list):
    """
    Prints a list of strings inside an ASCII box with the content vertically centered.
    """
    # Get the size of the terminal
    terminal_size = os.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines

    # Prepare the horizontal border
    horizontal_border = '+' + '-' * (width - 2) + '+'

    # Print the top border of the box
    print(horizontal_border)

    # Calculate the padding needed to center the text vertically
    padded_lines_above = (height - len(text_list)) // 2

    # Print the empty lines for top padding
    for _ in range(padded_lines_above - 1):  # -1 to account for the bottom border
        print('|' + ' ' * (width - 2) + '|')

    # Print the text lines, centered within the box
    for line in text_list:
        line_content = line.center(width - 2)
        print('|' + line_content + '|')

    # Print the prompt line
#    prompt_line = 'Type here: '
#    print('|' + prompt_line.center(width - 4) + '|')

    # Print the empty lines for bottom padding
    for _ in range(height - len(text_list) - padded_lines_above - 2):  # -2 to account for prompt line and top border
        print('|' + ' ' * (width - 2) + '|')

    # Print the bottom border of the box
    print(horizontal_border)

    # Get user input at the bottom of the terminal outside the box
    choice = input("Select option: ").upper()
    print('|' + choice.center(width - 4) + '|')

    return choice

def print_boxed_with_inputs(prompts):
    """
    Prints prompts inside an ASCII box and collects inputs for each prompt.
    """
    inputs = {}
    for prompt in prompts:
        print("+---------------------------------------------------+")
        # Center the prompt
        print("| " + prompt.center(50) + " |")
        print("+---------------------------------------------------+")
        # Collect input
        user_input = input(prompt + ": ").strip()
        inputs[prompt] = user_input
    return inputs

def print_boxed_with_inputs_modify(info_lines, input_prompts):
    """
    Prints information lines and input prompts inside an ASCII box and collects inputs.
    """
    inputs = {}
    
    # Print the top border of the box
    print("+---------------------------------------------------+")
    
    # Print the static information lines
    for line in info_lines:
        print("| " + line.center(50) + " |")
    
    # Print the input prompts and collect inputs
    for prompt in input_prompts:
        print("| " + prompt.ljust(50) + " |")
        print("+---------------------------------------------------+")
        user_input = input(prompt + ": ").strip()
        inputs[prompt] = user_input
    
    # Print the bottom border of the box
    print("+---------------------------------------------------+")
    
    return inputs
