# Do not remove credits given in this repo.
# Importing this repo instead of forking is strictly prohibited.
# Kindly fork and edit as you wish. Feel free to give credits to the developer(©️ AshinaXD).

from pyrogram import Client
from config import Config
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Suppress Pyrogram logs
pyrogram_logger = logging.getLogger("pyrogram")
pyrogram_logger.setLevel(logging.WARNING)

# Load configuration from config.py
API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
MAIN_CHANNEL = Config.MAIN_CHANNEL
TIMEZONE = Config.TIMEZONE
SUDO_USERS = Config.SUDO_USERS
WEBHOOK = Config.WEBHOOK

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
