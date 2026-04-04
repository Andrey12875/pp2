import curses
import db_functions
import curses
import db_functions

def pattern(stdscr):
    pattern_text = ""
    result = []

    while True:
        stdscr.clear()

        stdscr.addstr(2, 4, "Pattern search", curses.A_BOLD)
        stdscr.addstr(5, 4, "Pattern:", curses.A_REVERSE)
        stdscr.addstr(5, 20, pattern_text, curses.A_NORMAL)

        stdscr.addstr(7, 4, "Press SPACE on Pattern to enter text", curses.A_NORMAL)
        stdscr.addstr(8, 4, "Press ESC to exit", curses.A_NORMAL)

        stdscr.addstr(10, 4, "id|first_name|last_name|number", curses.A_NORMAL)

        for i, item in enumerate(result):
            row_text = "|".join(map(str, item))
            stdscr.addstr(11 + i, 4, row_text, curses.A_NORMAL)

        stdscr.refresh()
        key = stdscr.getch()

        if key == 27:
            return

        if key == ord(" "):
            stdscr.addstr(5, 20, " " * 20, curses.A_NORMAL)
            curses.echo()
            pattern_text = stdscr.getstr(5, 20, 20).decode()
            curses.noecho()

            result = db_functions.find_by_pattern(pattern_text)
