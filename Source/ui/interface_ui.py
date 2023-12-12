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
