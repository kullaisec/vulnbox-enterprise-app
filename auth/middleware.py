from utils.helpers import load_session
from flask import request

def authenticate():
    raw = request.cookies.get("session")
    return load_session(raw.encode())
