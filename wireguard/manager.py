import sqlite3
import subprocess

DB_FILE = "vpn.db"


def get_next_ip():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("SELECT vpn_ip FROM users WHERE vpn_ip IS NOT NULL")

    used = {
        row[0].split(".")[-1]
        for row in cur.fetchall()
    }

    conn.close()

    for i in range(2, 255):
        if str(i) not in used:
            return f"10.77.77.{i}"

    raise RuntimeError("Свободных IP нет")


def generate_keys():
    """
    Генерация пары ключей WireGuard.
    Возвращает (private_key, public_key).
    """

    private_key = subprocess.check_output(
        ["wg", "genkey"],
        text=True
    ).strip()

    public_key = subprocess.check_output(
        ["wg", "pubkey"],
        input=private_key,
        text=True
    ).strip()

    return private_key, public_key


def create_client():
    """
    Создаёт нового VPN-клиента.
    Пока только генерирует IP и ключи.
    """

    vpn_ip = get_next_ip()
    private_key, public_key = generate_keys()

    return {
        "vpn_ip": vpn_ip,
        "private_key": private_key,
        "public_key": public_key,
    }
