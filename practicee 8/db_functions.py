import db

def find_by_pattern(data):
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM pattern_match(%s)",
                (data,)
            )
            return cur.fetchall()

def insert_name_phone(name, surname, phone):
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM insert_name_phone(%s, %s, %s)",
                (name, surname, phone)
            )

def list_insert(names, surnames, phones):
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM insert_many_users(%s, %s, %s)",
                (names, surnames, phones)
            )
            return cur.fetchall()

def deleting_by_name(name, phone):
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM delete_by_name_or_phone(%s, %s)",
                (name,phone)
            )