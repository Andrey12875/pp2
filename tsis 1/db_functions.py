import db

def find_by_pattern(data):
    with db.connect() as conn:
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
                WHERE contacts.first_name ILIKE %s
                   OR contacts.last_name ILIKE %s
                   OR contacts.email ILIKE %s
                   OR groups.name ILIKE %s
                   OR phones.number ILIKE %s
                   OR phones.phone_type ILIKE %s
                ORDER BY contacts.id
                """,
                (
                    data + "%",
                    data + "%",
                    data + "%",
                    data + "%",
                    data + "%",
                    data + "%"
                )
            )
            return cur.fetchall()

def insert_contact(first_name, last_name, email, birthday, group_name, phone, phone_type):
    with db.connect() as conn:
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

            cur.execute(
                """
                INSERT INTO phones (contact_id, number, phone_type)
                VALUES (%s, %s, %s)
                """,
                (contact_id, phone, phone_type)
            )

            return True

def list_insert(first_names, last_names, emails, birthdays, group_names, phones, phone_types):
    incorrect = []

    if not (
        len(first_names) == len(last_names) == len(emails) ==
        len(birthdays) == len(group_names) == len(phones) == len(phone_types)
    ):
        return [("different list lengths",)]

    allowed_types = ["home", "work", "mobile"]

    with db.connect() as conn:
        with conn.cursor() as cur:
            for i in range(len(first_names)):
                first_name = first_names[i].strip()
                last_name = last_names[i].strip()
                email = emails[i].strip()
                birthday = birthdays[i].strip()
                group_name = group_names[i].strip()
                phone = phones[i].strip()
                phone_type = phone_types[i].strip()

                if phone_type not in allowed_types:
                    incorrect.append((first_name, last_name, phone, "wrong phone type"))
                    continue

                cur.execute(
                    """
                    SELECT id FROM groups
                    WHERE name = %s
                    """,
                    (group_name,)
                )

                group = cur.fetchone()

                if group is None:
                    incorrect.append((first_name, last_name, phone, "wrong group"))
                    continue

                cur.execute(
                    """
                    SELECT id FROM phones
                    WHERE number = %s
                    """,
                    (phone,)
                )

                duplicate_phone = cur.fetchone()

                if duplicate_phone is not None:
                    incorrect.append((first_name, last_name, phone, "phone already exists"))
                    continue

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

    return incorrect

def deleting_by_name(name, phone):
    with db.connect() as conn:
        with conn.cursor() as cur:
            if phone != "":
                cur.execute(
                    """
                    SELECT contact_id
                    FROM phones
                    WHERE number = %s
                    """,
                    (phone,)
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

            elif name != "":
                cur.execute(
                    """
                    DELETE FROM contacts
                    WHERE first_name = %s
                    """,
                    (name,)
                )

                return bool(cur.rowcount)

            return False

