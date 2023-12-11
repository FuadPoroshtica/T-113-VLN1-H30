import curses

def interface(stdscr):
    stdscr.clear()
    COLOR_PAIR_ID = 1
    initialize_color(stdscr, COLOR_PAIR_ID)
    add_lines(stdscr, COLOR_PAIR_ID)
    stdscr.refresh()
    stdscr.getkey()


def initialize_color(stdscr, color_pair_id):
    curses.init_pair(color_pair_id, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.attron(curses.color_pair(color_pair_id))
    stdscr.box()
    stdscr.attroff(curses.color_pair(color_pair_id))


def add_lines(stdscr, color_pair_id):
    for i in range
