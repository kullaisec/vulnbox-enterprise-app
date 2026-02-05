from utils.http import fetch_url

def process(data):
    callback = data.get("callback_url")
    return fetch_url(callback)
