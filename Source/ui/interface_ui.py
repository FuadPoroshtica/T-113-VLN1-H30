import os

def interface(text_list):
    os.system('cls' if os.name == 'nt' else 'clear')
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
