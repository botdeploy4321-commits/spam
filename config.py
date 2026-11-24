# config.py
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==== Telegram API Credentials ====
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# ==== Bot Token ====
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==== Owner Info ====
OWNER_NAME = os.getenv("OWNER_NAME", "Unknown")

# ==== Session Storage Directory ====
SESSION_DIR = os.getenv("SESSION_DIR", "sessions")
