import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    MAIN_CHANNEL = os.environ.get("MAIN_CHANNEL", "")
    MESSAGE_ID = int(os.environ.get("MESSAGE_ID", ""))
    TIMEZONE = os.environ.get("TIMEZONE", "")