import os

def cleanup(path):
    if os.path.exists(path):
        os.remove(path)
