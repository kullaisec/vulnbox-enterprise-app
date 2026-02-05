from users.repository import fetch_user

def get_user_by_email(email):
    return fetch_user(email)
