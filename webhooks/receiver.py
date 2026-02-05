from flask import request
from webhooks.processor import process

def webhook():
    return process(request.json)
