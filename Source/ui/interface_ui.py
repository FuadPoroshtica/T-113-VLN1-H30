import curses

def interface(stdscr):
    stdscr.clear()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.attron(curses.color_pair(1))
    stdscr.box()
    stdscr.attroff(curses.color_pair(1))

    for i in range(1, 10):
        stdscr.addstr(i, 1, '10 divided by {} is {}'.format(i,
                                                            10 // i))

    stdscr.refresh()
    stdscr.getkey()