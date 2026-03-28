import curses
import db

def showing(stdscr):
    current_row = 0
    menu = ["First name", "Last name", "Number", "Exit"]
    data = ["","", ""]
    while True:
        stdscr.clear()
        for i, item in enumerate(menu):
            if i == current_row:
                stdscr.addstr(i + 5, 4, item, curses.A_REVERSE)
                if i<3:
                    stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)

            else:
                stdscr.addstr(i + 5, 4, item, curses.A_NORMAL)
                if i < 3:
                    stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_DOWN and current_row < 3:
            current_row += 1
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        if key == ord(" ") and current_row < 2:
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 20, 20).decode()
            curses.noecho()
        if key == ord(" ") and current_row == 2:
            data[2] =  db.find_member(data[0], data[1])
        if key == ord(" ") and current_row == 3:
            return 0


def deleting(stdscr):
    current_row = 0
    menu = ["Number","Delete", "Exit", ""]
    data = [""]
    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            if i == current_row:
                stdscr.addstr(i + 5, 4, item, curses.A_REVERSE)
                if i < 1:
                    stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)

            else:
                stdscr.addstr(i + 5, 4, item, curses.A_NORMAL)
                if i < 1:
                    stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_DOWN and current_row <2:
            current_row += 1
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        if key == ord(" ") and current_row < 1:
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 20, 20).decode()
            curses.noecho()
        if key == ord(" ") and current_row == 1:
            if db.delete_member(data[0]) == True:
                menu[3] = "Deleted"
            else:
                menu[3] = "Not found"
        if key == ord(" ") and current_row == 2:
            return 0


def updating(stdscr):
    current_row = 0
    menu = ["Number", "First name", "Last name", "New name", "New surname", "New number", "Save", "Exit"]
    data = ["", "", "", "", "", ""]
    status = ""

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            if i < 3:
                y = i + 5
                x = 4
                value_x = 20
            elif i < 6:
                y = i + 2
                x = 30
                value_x = 48
            else:
                y = i + 2
                x = 4
                value_x = None

            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(y, x, item, attr)

            if i < 6:
                stdscr.addstr(y, value_x, data[i], curses.A_NORMAL)

        stdscr.addstr(12, 4, status, curses.A_NORMAL)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 7:
            current_row += 1
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row == 0:
            curses.echo()
            data[0] = stdscr.getstr(5, 20, 20).decode()
            curses.noecho()

            member = db.find_by_number(data[0])

            if member is None:
                data[1] = ""
                data[2] = ""
                data[3] = ""
                data[4] = ""
                data[5] = ""
                status = "Not found"
            else:
                data[1] = member[0]
                data[2] = member[1]
                data[3] = member[0]
                data[4] = member[1]
                data[5] = data[0]
                status = "Found"

        if key == ord(" ") and current_row == 3:
            curses.echo()
            data[3] = stdscr.getstr(5, 48, 20).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 4:
            curses.echo()
            data[4] = stdscr.getstr(6, 48, 20).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 5:
            curses.echo()
            data[5] = stdscr.getstr(7, 48, 20).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 6:
            new_data = [data[3], data[4], data[5]]
            if db.update_member(data[0], new_data):
                data[0] = data[5]
                data[1] = data[3]
                data[2] = data[4]
                status = "Updated"
            else:
                status = "Update failed"

        if key == ord(" ") and current_row == 7:
            return

def adding(stdscr):
    current_row = 0
    menu = ["First name", "Last name", "phone number", "Save", "Exit"]
    data = ["", "", ""]
    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            if i == current_row:
                stdscr.addstr(i + 5, 4, item, curses.A_REVERSE)
                if i < 3:
                    stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)

            else:
                stdscr.addstr(i + 5, 4, item, curses.A_NORMAL)
                if i < 3:
                     stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            current_row += 1
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        if key == ord(" ") and current_row < 3:
            curses.echo()
            data[current_row] = stdscr.getstr(current_row+5, 20, 20).decode()
            curses.noecho()
        if key == ord(" ") and current_row == 3:
            db.insert_member(data)
            stdscr.addstr(3 + 5, 20, "SAVED", curses.A_NORMAL)
        if key == ord(" ") and current_row == 4:
            return 0
def main(stdscr):
    menu = ["Add member", "Update member", "Delete member", "Show data", "Exit"]
    current_row = 0

    while True:
        stdscr.clear()
        for i, item in enumerate(menu):
            if i == current_row:
                stdscr.addstr(i+5, 4, item, curses.A_REVERSE)
            else:
                stdscr.addstr(i+5, 4, item, curses.A_NORMAL)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            current_row += 1
        if key == curses.KEY_UP and current_row >0:
            current_row -= 1
        if key == ord(" "):
            if current_row == 4:
                break
            elif current_row == 0:
               adding(stdscr)
            elif current_row == 1:
                updating(stdscr)
            elif current_row == 2:
                deleting(stdscr)
            elif current_row == 3:
                showing(stdscr)




curses.wrapper(main)