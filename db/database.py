import sqlite3
import threading

_db_lock = threading.Lock()
_connection = None

def get_db():
    global _connection

    if _connection is None:
        _connection = sqlite3.connect(
            "/tmp/app.db",
            check_same_thread=False
        )

        _connection.isolation_level = None

    return _connection
