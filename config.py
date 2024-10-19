import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    MAIN_CHANNEL = os.environ.get("MAIN_CHANNEL", "")
    TIMEZONE = os.environ.get("TIMEZONE", "")
    WEBHOOK = os.environ.get("WEBHOOK", "False").lower() == "true"
    SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split(','))) if os.environ.get("SUDO_USERS") else []
