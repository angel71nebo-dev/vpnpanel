import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# WireGuard
WG_INTERFACE = os.getenv("WG_INTERFACE", "wg0")
WG_NETWORK = os.getenv("WG_NETWORK", "10.77.77")
SERVER_PUBLIC_IP = os.getenv("SERVER_PUBLIC_IP", "")
CLIENT_DIR = Path(os.getenv("CLIENT_DIR", "/etc/wireguard/clients"))

WG_CONF = Path(f"/etc/wireguard/{WG_INTERFACE}.conf")

# Проект
DB_FILE = BASE_DIR / "db.json"
LOG_DIR = BASE_DIR / "logs"
BACKUP_DIR = BASE_DIR / "backups"

LOG_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)
CLIENT_DIR.mkdir(parents=True, exist_ok=True)
