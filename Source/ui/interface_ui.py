import os
import cursor

def interface(text_list):
    cursor.hide()
    try:
        terminal_size = os.get_terminal_size()
        width = terminal_size.columns
        height = terminal_size.lines
    except OSError:
        width = 100
        height = 30

    horizontal_border = '+' + '-' * (width - 2) + '+'
    print(horizontal_border)
    padded_lines_above = (height - len(text_list)) // 2

    for _ in range(padded_lines_above - 1):
        print('|' + ' ' * (width - 2) + '|')

    for line in text_list:
        line_content = line.center(width - 2)
        print('|' + line_content + '|')

    for _ in range(height - len(text_list) - padded_lines_above - 2):
        print('|' + ' ' * (width - 2) + '|')

    print(horizontal_border)

    return interface


def print_boxed_with_inputs(prompts):
    inputs = {}
    cursor.hide()
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns
    terminal_height = terminal_size.lines

    while True:
        total_content_lines = len(prompts) * 2
        empty_lines = max(0, terminal_height - total_content_lines - 2)
        padding_above_and_below = empty_lines // 2

        horizontal_border = '+' + '-' * (terminal_width - 2) + '+'
        print(horizontal_border)

        for _ in range(padding_above_and_below):
            print('|' + ' ' * (terminal_width - 2) + '|')

        for prompt in prompts:
            prompt_line = "| " + prompt.ljust(terminal_width - 4) + " |"
            print(prompt_line)
            cursor.show()
            user_input = input('| ' + ' ' * (terminal_width - 4) + '| ' + prompt + ": ").strip()
            cursor.hide()
            inputs[prompt] = user_input

        for _ in range(empty_lines - padding_above_and_below):
            print('|' + ' ' * (terminal_width - 2) + '|')

        print(horizontal_border)

        if "quit" in inputs.values():
            cursor.show()
            break

    cursor.show()
    return inputs

