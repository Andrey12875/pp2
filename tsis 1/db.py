import psycopg
import json
import csv
def connect():
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="phonebook",
        user="postgres",
        password="3031028"
    )
    return conn

def insert_member(data):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO person (first_name, last_name, number) VALUES (%s, %s ,%s)",
                (data[0],data[1],data[2])
            )
def find_member(first_name, last_name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    contacts.id,
                    contacts.first_name,
                    contacts.last_name,
                    contacts.email,
                    contacts.birthday,
                    groups.name,
                    phones.number,
                    phones.phone_type
                FROM contacts
                LEFT JOIN groups ON contacts.group_id = groups.id
                LEFT JOIN phones ON contacts.id = phones.contact_id
                WHERE contacts.first_name = %s 
                  AND contacts.last_name = %s
                ORDER BY contacts.id
                """,
                (first_name, last_name)
            )

            rows = cur.fetchall()

            if not rows:
                return []

            return rows

def delete_member(number):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT contact_id
                FROM phones
                WHERE number = %s
                """,
                (number,)
            )

            row = cur.fetchone()

            if row is None:
                return False

            contact_id = row[0]

            cur.execute(
                """
                DELETE FROM contacts
                WHERE id = %s
                """,
                (contact_id,)
            )

            return bool(cur.rowcount)
def find_by_number(number):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    contacts.id,
                    contacts.first_name,
                    contacts.last_name,
                    contacts.email,
                    contacts.birthday,
                    groups.name,
                    phones.number,
                    phones.phone_type
                FROM contacts
                LEFT JOIN groups ON contacts.group_id = groups.id
                LEFT JOIN phones ON contacts.id = phones.contact_id
                WHERE phones.number = %s
                """,
                (number,)
            )

            row = cur.fetchone()
            return row
def update_member(old_number, new_data):
    first_name = new_data[0]
    last_name = new_data[1]
    email = new_data[2]
    birthday = new_data[3]
    group_name = new_data[4]
    new_number = new_data[5]
    phone_type = new_data[6]

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT contact_id
                FROM phones
                WHERE number = %s
                """,
                (old_number,)
            )

            row = cur.fetchone()

            if row is None:
                return False

            contact_id = row[0]

            cur.execute(
                """
                SELECT id
                FROM groups
                WHERE name = %s
                """,
                (group_name,)
            )

            group = cur.fetchone()

            if group is None:
                return False

            group_id = group[0]

            cur.execute(
                """
                UPDATE contacts
                SET first_name = %s,
                    last_name = %s,
                    email = %s,
                    birthday = %s,
                    group_id = %s
                WHERE id = %s
                """,
                (first_name, last_name, email, birthday, group_id, contact_id)
            )

            cur.execute(
                """
                UPDATE phones
                SET number = %s,
                    phone_type = %s
                WHERE contact_id = %s
                  AND number = %s
                """,
                (new_number, phone_type, contact_id, old_number)
            )

            return True
def print_content():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT 
                    contacts.id,
                    contacts.first_name,
                    contacts.last_name,
                    contacts.email,
                    contacts.birthday,
                    groups.name,
                    phones.number,
                    phones.phone_type
                FROM contacts
                LEFT JOIN groups ON contacts.group_id = groups.id
                LEFT JOIN phones ON contacts.id = phones.contact_id
                ORDER BY contacts.id
                """
            )
            return cur.fetchall()

def csv_read(filename):
    imported = 0
    skipped = 0

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            contact = {
                "first_name": row["first_name"].strip(),
                "last_name": row["last_name"].strip(),
                "email": row["email"].strip(),
                "birthday": row["birthday"].strip(),
                "group": row["group"].strip(),
                "phones": [
                    {
                        "number": row["number"].strip(),
                        "phone_type": row["phone_type"].strip()
                    }
                ]
            }

            try:
                if insert_contact_with_phones(contact):
                    imported += 1
                else:
                    skipped += 1
            except Exception:
                skipped += 1

    return imported, skipped
def add_contact(data):
    first_name = data[0]
    last_name = data[1]
    email = data[2]
    birthday = data[3]
    group_name = data[4]
    phone = data[5]
    phone_type = data[6]

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM groups WHERE name = %s",
                (group_name,)
            )
            group = cur.fetchone()

            if group is None:
                return False

            group_id = group[0]

            cur.execute(
                """
                INSERT INTO contacts (first_name, last_name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (first_name, last_name, email, birthday, group_id)
            )

            contact_id = cur.fetchone()[0]

            cur.execute(
                """
                INSERT INTO phones (contact_id, number, phone_type)
                VALUES (%s, %s, %s)
                """,
                (contact_id, phone, phone_type)
            )

            return True

def add_phone_to_contact(contact_id, number, phone_type):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO phones (contact_id, number, phone_type)
                VALUES (%s, %s, %s)
                """,
                (contact_id, number, phone_type)
            )
            return True

def export_to_json(filename):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    contacts.id,
                    contacts.first_name,
                    contacts.last_name,
                    contacts.email,
                    contacts.birthday,
                    groups.name,
                    phones.number,
                    phones.phone_type
                FROM contacts
                LEFT JOIN groups ON contacts.group_id = groups.id
                LEFT JOIN phones ON contacts.id = phones.contact_id
                ORDER BY contacts.id
                """
            )

            rows = cur.fetchall()

    contacts_dict = {}

    for row in rows:
        contact_id = row[0]

        if contact_id not in contacts_dict:
            contacts_dict[contact_id] = {
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "birthday": str(row[4]) if row[4] is not None else "",
                "group": row[5],
                "phones": []
            }

        if row[6] is not None:
            contacts_dict[contact_id]["phones"].append(
                {
                    "number": row[6],
                    "phone_type": row[7]
                }
            )

    contacts_list = list(contacts_dict.values())

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts_list, file, indent=4, ensure_ascii=False)

    return True

def insert_contact_with_phones(contact):
    first_name = contact["first_name"]
    last_name = contact["last_name"]
    email = contact["email"]
    birthday = contact["birthday"]
    group_name = contact["group"]
    phones = contact["phones"]

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id FROM groups
                WHERE name = %s
                """,
                (group_name,)
            )

            group = cur.fetchone()

            if group is None:
                return False

            group_id = group[0]

            cur.execute(
                """
                INSERT INTO contacts (first_name, last_name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (first_name, last_name, email, birthday, group_id)
            )

            contact_id = cur.fetchone()[0]

            for phone in phones:
                cur.execute(
                    """
                    INSERT INTO phones (contact_id, number, phone_type)
                    VALUES (%s, %s, %s)
                    """,
                    (
                        contact_id,
                        phone["number"],
                        phone["phone_type"]
                    )
                )

            return True

def import_from_json(filename, duplicate_action):
    with open(filename, "r", encoding="utf-8") as file:
        contacts = json.load(file)

    imported = 0
    skipped = 0
    overwritten = 0

    for contact in contacts:
        first_name = contact["first_name"]
        last_name = contact["last_name"]

        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id FROM contacts
                    WHERE first_name = %s AND last_name = %s
                    """,
                    (first_name, last_name)
                )

                duplicate = cur.fetchone()

                if duplicate is not None:
                    if duplicate_action == "skip":
                        skipped += 1
                        continue

                    elif duplicate_action == "overwrite":
                        cur.execute(
                            """
                            DELETE FROM contacts
                            WHERE first_name = %s AND last_name = %s
                            """,
                            (first_name, last_name)
                        )
                        overwritten += 1

                    else:
                        skipped += 1
                        continue

        if insert_contact_with_phones(contact):
            imported += 1
        else:
            skipped += 1

    return imported, skipped, overwritten