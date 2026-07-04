import sqlite3
from pathlib import Path

DB_FILE = Path("vpn.db")


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        cur = self.conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            username TEXT,
            client_name TEXT UNIQUE,
            public_key TEXT,
            vpn_ip TEXT UNIQUE,
            created_at TEXT,
            expires_at TEXT,
            status TEXT DEFAULT 'active'
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS servers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            host TEXT,
            wg_interface TEXT,
            network TEXT,
            public_ip TEXT,
            active INTEGER DEFAULT 1
        )
        """)

        self.conn.commit()


if __name__ == "__main__":
    db = Database()
    print("Database created successfully.")
