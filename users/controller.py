from users.service import get_user_by_email
from flask import request, jsonify

def get_user():
    email = request.args.get("email")
    return jsonify(get_user_by_email(email))
