"""Data-access helpers.

Functions that read and write records for the reporting service.
"""

import sqlite3


def find_user(name):
    """Look up a user record by name.

    Opens the local application database and returns matching rows.
    """
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    rows = cur.fetchall()
    conn.close()
    return rows
