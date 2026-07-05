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
        cur.execute("""
        CREATE TABLE IF NOT EXISTS vpn_clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            client_name TEXT,
            vpn_ip TEXT UNIQUE,
            private_key TEXT,
            public_key TEXT,
            server TEXT,
            created_at TEXT,
            status TEXT DEFAULT 'active'
        )
        """)
        self.conn.commit()

    def get_user(self, telegram_id: int):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE telegram_id = ?",
            (telegram_id,)
        )
        return cur.fetchone()

    def add_user(self, telegram_id: int, username: str):
        cur = self.conn.cursor()

        cur.execute(
            """
            INSERT INTO users (
                telegram_id,
                username,
                created_at
            )
            VALUES (?, ?, datetime('now'))
            """,
            (
                telegram_id,
                username,
            )
        )

        self.conn.commit()

    def update_username(self, telegram_id: int, username: str):
        cur = self.conn.cursor()

        cur.execute(
            """
            UPDATE users
            SET username = ?
            WHERE telegram_id = ?
            """,
            (
                username,
                telegram_id,
            )
        )

        self.conn.commit()
    def add_vpn_client(
        self,
        telegram_id: int,
        client_name: str,
        vpn_ip: str,
        private_key: str,
        public_key: str,
        server: str,
    ):
        cur = self.conn.cursor()

        cur.execute(
            """
            INSERT INTO vpn_clients (
                telegram_id,
                client_name,
                vpn_ip,
                private_key,
                public_key,
                server,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
            """,
            (
                telegram_id,
                client_name,
                vpn_ip,
                private_key,
                public_key,
                server,
            )
        )

        self.conn.commit()


    def get_vpn_clients(self, telegram_id: int):
        cur = self.conn.cursor()

        cur.execute(
            """
            SELECT *
            FROM vpn_clients
            WHERE telegram_id = ?
            ORDER BY id
            """,
            (telegram_id,)
        )

        return cur.fetchall()


if __name__ == "__main__":
    db = Database()
    print("Database created successfully.")
