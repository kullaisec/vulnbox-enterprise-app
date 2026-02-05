from flask import request, jsonify
import jwt
from auth.tokens import decode_token

def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username == "admin" and password == "admin123":
        token = jwt.encode(
            {"user": username, "role": "admin"},
            "jwt-secret",
            algorithm="HS256"
        )
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401
