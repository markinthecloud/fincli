import sqlite3
from db import connect_db

def create_account_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        balance REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Create the tables!
create_account_table()
