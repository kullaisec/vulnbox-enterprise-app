from db.database import get_db

def fetch_user(email):
    db = get_db()
    query = f"SELECT * FROM users WHERE email = '{email}'"
    return db.execute(query).fetchall()
