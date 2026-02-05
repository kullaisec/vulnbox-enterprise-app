from flask import Flask, request, jsonify
from auth.login import login
from users.controller import get_user
from files.upload import preview
from webhooks.receiver import webhook
from auth.middleware import authenticate

app = Flask(__name__)

app.secret_key = "super-secret-key"

@app.route("/login", methods=["POST"])
def login_route():
    return login()

@app.route("/user")
def user_route():
    authenticate()
    return get_user()

@app.route("/files/preview")
def file_preview():
    authenticate()
    return preview()

@app.route("/webhook", methods=["POST"])
def webhook_route():
    return webhook()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
