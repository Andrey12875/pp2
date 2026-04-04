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


def inserting(stdscr):
    current_row = 0
    menu = ["First name", "Last name", "Phone number", "Save", "Exit"]
    data = ["", "", ""]
    status = ""

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(i + 5, 4, item, attr)

            if i < 3:
                stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)

        stdscr.addstr(11, 4, status, curses.A_NORMAL)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 4:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row < 3:
            stdscr.addstr(current_row + 5, 20, " " * 20, curses.A_NORMAL)
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 20, 20).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 3:
            try:
                db_functions.insert_name_phone(data[0], data[1], data[2])
                status = "Saved"
            except Exception:
                status = "Error"

        if key == ord(" ") and current_row == 4:
            return

def list_insert(stdscr):
    current_row = 0
    menu = ["First name", "Last name", "Phone number", "Save", "Exit"]
    data = ["", "", ""]
    status = ""
    result = []

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(i + 5, 4, item, attr)

            if i < 3:
                stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)

        stdscr.addstr(11, 4, status, curses.A_NORMAL)

        for i, item in enumerate(result):
            row_text = " | ".join(map(str, item))
            stdscr.addstr(13 + i, 4, row_text, curses.A_NORMAL)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 4:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row < 3:
            stdscr.addstr(current_row + 5, 20, " " * 20, curses.A_NORMAL)
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 20, 20).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 3:
            result = db_functions.list_insert(
                data[0].split(","),
                data[1].split(","),
                data[2].split(",")
            )

            if result:
                status = "Incorrect data found"
            else:
                status = "Saved"

        if key == ord(" ") and current_row == 4:
            return

def deleting_by_name(stdscr):
    current_row = 0
    menu = ["First name", "Phone number", "Delete", "Exit"]
    data = ["", ""]
    status = ""


    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(i + 5, 4, item, attr)

            if i < 2:
                stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)

        stdscr.addstr(10, 4, status, curses.A_NORMAL)



        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 3:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row < 2:
            stdscr.addstr(current_row + 5, 20, " " * 20, curses.A_NORMAL)
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 20, 20).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 2:
            result = db_functions.deleting_by_name(data[0], data[1])

            if result:
                status = "Deleted"
            else:
                status = "Deleted"

        if key == ord(" ") and current_row == 3:
            return
