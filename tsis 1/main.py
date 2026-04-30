import curses
import db
import functions
def contents(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "exit", curses.A_REVERSE)
        stdscr.addstr(4, 4, "id|name|surname|email|birthday|group|phone number|phone type", curses.A_NORMAL)
        for i, item in enumerate(db.print_content()):
            put = "|".join(map(str,item))
            stdscr.addstr(i + 5, 4, put, curses.A_NORMAL)
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord(" "): return None

def functions_menu(stdscr):
    menu = ["Find by pattern","inserting by name and phone", "insert with list", "deleting", "Exit"]
    current_row = 0

    while True:
        stdscr.clear()
        for i, item in enumerate(menu):
            if i == current_row:
                stdscr.addstr(i + 5, 4, item, curses.A_REVERSE)
            else:
                stdscr.addstr(i + 5, 4, item, curses.A_NORMAL)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            current_row += 1
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        if key == ord(" "):
            if current_row == 4:
                return None
            elif current_row == 0:
                functions.pattern(stdscr)
            elif current_row == 1:
                functions.inserting(stdscr)
            elif current_row == 2:
                functions.list_insert(stdscr)
            elif current_row == 3:
                functions.deleting_by_name(stdscr)

def showing(stdscr):
    current_row = 0
    menu = ["First name", "Last name", "Search", "Exit"]
    data = ["", ""]
    result = []

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(i + 5, 4, item, attr)

            if i < 2:
                stdscr.addstr(i + 5, 20, data[i], curses.A_NORMAL)

        stdscr.addstr(10, 4, "id|first_name|last_name|email|birthday|group|number|phone_type", curses.A_NORMAL)

        for i, item in enumerate(result):
            row_text = "|".join(map(str, item))
            stdscr.addstr(11 + i, 4, row_text, curses.A_NORMAL)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 3:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row < 2:
            stdscr.addstr(current_row + 5, 20, " " * 25, curses.A_NORMAL)
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 20, 25).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 2:
            result = db.find_member(data[0], data[1])

        if key == ord(" ") and current_row == 3:
            return


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

    menu = [
        "Search by number",
        "First name",
        "Last name",
        "Email",
        "Birthday YYYY-MM-DD",
        "Group Family Work Friend Other",
        "Phone number",
        "Phone type home work mobile",
        "Save",
        "Exit"
    ]

    data = ["", "", "", "", "", "", ""]
    old_number = ""
    status = ""

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(i + 5, 4, item, attr)

            if i < 8:
                if i == 0:
                    stdscr.addstr(i + 5, 42, old_number, curses.A_NORMAL)
                else:
                    stdscr.addstr(i + 5, 42, data[i - 1], curses.A_NORMAL)

        stdscr.addstr(17, 4, status, curses.A_NORMAL)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 9:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row == 0:
            stdscr.addstr(5, 42, " " * 30, curses.A_NORMAL)
            curses.echo()
            old_number = stdscr.getstr(5, 42, 30).decode()
            curses.noecho()

            member = db.find_by_number(old_number)

            if member is None:
                data = ["", "", "", "", "", "", ""]
                status = "Not found"
            else:
                data[0] = member[1]
                data[1] = member[2]
                data[2] = member[3]
                data[3] = str(member[4])
                data[4] = member[5]
                data[5] = member[6]
                data[6] = member[7]
                status = "Found"

        if key == ord(" ") and 1 <= current_row <= 7:
            stdscr.addstr(current_row + 5, 42, " " * 30, curses.A_NORMAL)
            curses.echo()
            data[current_row - 1] = stdscr.getstr(current_row + 5, 42, 30).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 8:
            if db.update_member(old_number, data):
                old_number = data[5]
                status = "Updated"
            else:
                status = "Update failed"

        if key == ord(" ") and current_row == 9:
            return

def adding(stdscr):
    current_row = 0
    menu = [
        "First name",
        "Last name",
        "Email",
        "Birthday YYYY-MM-DD",
        "Group Family Work Friend Other",
        "Phone number",
        "Phone type home work mobile",
        "Save",
        "Exit"
    ]

    data = ["", "", "", "", "", "", ""]
    status = ""

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            if i == current_row:
                stdscr.addstr(i + 5, 4, item, curses.A_REVERSE)
            else:
                stdscr.addstr(i + 5, 4, item, curses.A_NORMAL)

            if i < 7:
                stdscr.addstr(i + 5, 40, data[i], curses.A_NORMAL)

        stdscr.addstr(15, 4, status, curses.A_NORMAL)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 8:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row < 7:
            stdscr.addstr(current_row + 5, 40, " " * 30, curses.A_NORMAL)
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 40, 30).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 7:
            if db.add_contact(data):
                status = "Saved"
            else:
                status = "Wrong group"

        if key == ord(" ") and current_row == 8:
            return
def add_phone(stdscr):
    current_row = 0
    menu = ["Contact id", "Phone number", "Phone type home work mobile", "Save", "Exit"]
    data = ["", "", ""]
    status = ""

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(i + 5, 4, item, attr)

            if i < 3:
                stdscr.addstr(i + 5, 40, data[i], curses.A_NORMAL)

        stdscr.addstr(12, 4, status, curses.A_NORMAL)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < 4:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row < 3:
            stdscr.addstr(current_row + 5, 40, " " * 30, curses.A_NORMAL)
            curses.echo()
            data[current_row] = stdscr.getstr(current_row + 5, 40, 30).decode()
            curses.noecho()

        if key == ord(" ") and current_row == 3:
            try:
                contact_id = int(data[0])
                db.add_phone_to_contact(contact_id, data[1], data[2])
                status = "Phone added"
            except ValueError:
                status = "Contact id must be number"
            except Exception:
                status = "Error"

        if key == ord(" ") and current_row == 4:
            return
def export_json_screen(stdscr):
    filename = ""

    stdscr.clear()
    stdscr.addstr(5, 4, "JSON filename:", curses.A_REVERSE)
    stdscr.refresh()

    curses.echo()
    filename = stdscr.getstr(5, 25, 100).decode()
    curses.noecho()

    try:
        db.export_to_json(filename)
        return "Exported to JSON"
    except Exception:
        return "Export error"
def import_json_screen(stdscr):
    filename = ""
    action = ""

    stdscr.clear()

    stdscr.addstr(5, 4, "JSON filename:", curses.A_REVERSE)
    curses.echo()
    filename = stdscr.getstr(5, 25, 100).decode()
    curses.noecho()

    stdscr.addstr(7, 4, "Duplicate action skip overwrite:", curses.A_REVERSE)
    curses.echo()
    action = stdscr.getstr(7, 40, 20).decode()
    curses.noecho()

    try:
        imported, skipped, overwritten = db.import_from_json(filename, action)

        return (
            "Imported: " + str(imported) +
            " Skipped: " + str(skipped) +
            " Overwritten: " + str(overwritten)
        )

    except Exception:
        return "Import JSON error"

def import_csv_screen(stdscr):
    filename = ""

    stdscr.clear()
    stdscr.addstr(5, 4, "CSV filename:", curses.A_REVERSE)
    stdscr.refresh()

    curses.echo()
    filename = stdscr.getstr(5, 25, 100).decode()
    curses.noecho()

    try:
        imported, skipped = db.csv_read(filename)

        return (
            "Imported: " + str(imported) +
            " Skipped: " + str(skipped)
        )

    except Exception:
        return "Import CSV error"


def import_export_menu(stdscr):
    current_row = 0

    menu = [
        "Export to JSON",
        "Import from JSON",
        "Import from CSV",
        "Exit"
    ]

    status = ""

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            attr = curses.A_REVERSE if i == current_row else curses.A_NORMAL
            stdscr.addstr(i + 5, 4, item, attr)

        stdscr.addstr(11, 4, status, curses.A_NORMAL)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        if key == ord(" ") and current_row == 0:
            status = export_json_screen(stdscr)

        if key == ord(" ") and current_row == 1:
            status = import_json_screen(stdscr)

        if key == ord(" ") and current_row == 2:
            status = import_csv_screen(stdscr)

        if key == ord(" ") and current_row == 3:
            return

def main(stdscr):
    menu = [
        "Add member",
        "Add phone",
        "Update member",
        "Delete member",
        "Show data",
        "Phonebook",
        "Functions",
        "Import Export",
        "Exit"
    ]
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
        if key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        if key == curses.KEY_UP and current_row >0:
            current_row -= 1
        if key == ord(" "):
            if current_row == 8:
                break

            elif current_row == 0:
                adding(stdscr)

            elif current_row == 1:
                add_phone(stdscr)

            elif current_row == 2:
                updating(stdscr)

            elif current_row == 3:
                deleting(stdscr)

            elif current_row == 4:
                showing(stdscr)

            elif current_row == 5:
                contents(stdscr)

            elif current_row == 6:
                functions_menu(stdscr)

            elif current_row == 7:
                import_export_menu(stdscr)




curses.wrapper(main)