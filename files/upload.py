from flask import request
from files.storage import read_file

def preview():
    name = request.args.get("name")
    return read_file(name)
