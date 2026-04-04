import psycopg
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
                "SELECT number FROM person WHERE first_name = %s AND last_name = %s",
                (first_name, last_name)
            )
            row = cur.fetchone()
            if row is None:
                return "Not found"
            return row[0]

def delete_member(number):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "Delete FROM person WHERE number = %s",
                (number,)
            )
            return bool(cur.rowcount)

def find_by_number(number):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT first_name, last_name FROM person WHERE number = %s",
                (number,)
            )
            row = cur.fetchone()
            return row
def update_member(number, new_data):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE person SET first_name = %s, last_name = %s, number = %s WHERE number = %s",
                (new_data[0], new_data[1], new_data[2], number)
            )
            return bool(cur.rowcount)
def print_content():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM person"
            )
            return cur.fetchall()

def csv_read(filename):
    with connect() as conn:
        with conn.cursor() as cur:
            file = open(filename)
            next(file)
            for line in file:
                info = [x.strip() for x in line.split(",")]
                if info[2].isdigit():
                    cur.execute(
                        "INSERT INTO person (first_name, last_name, number) VALUES (%s, %s, %s)",
                        (info[0], info[1], info[2])
                    )
def conflict_insert(data):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO person (first_name, last_name, number)
                VALUES (%s, %s, %s)
                ON CONFLICT (number) DO UPDATE
                SET first_name = EXCLUDED.first_name,
                    last_name = EXCLUDED.last_name
                """,
                (data[0], data[1], data[2])
            )