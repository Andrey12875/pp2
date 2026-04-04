import db

def find_by_pattern(data):
    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM pattern_match(%s)",
                (data,)
            )
            return cur.fetchall()