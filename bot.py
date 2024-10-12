import os
import logging
import asyncio
import json
import random
from datetime import datetime
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
import signal
import sys
from config import Config

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
MESSAGE_ID = Config.MESSAGE_ID
TIMEZONE = Config.TIMEZONE

IMAGE_DIR = "images"

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Global variable to store the latest schedule caption
latest_caption = ""

# Check if the image directory exists
if not os.path.isdir(IMAGE_DIR):
    logger.error(f"{IMAGE_DIR} is not a valid directory.")
    exit(1)

def get_random_image() -> str:
    """Return a random image path from the images directory."""
    images = [img for img in os.listdir(IMAGE_DIR) if img.endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        logger.error("No images found in the directory.")
        return None
    selected_image = random.choice(images)
    logger.info(f"Selected image: {selected_image}")
    return os.path.join(IMAGE_DIR, selected_image)

async def update_schedule() -> None:
    """Fetch and update today's anime schedule."""
    global latest_caption
    try:
        schedule_url = f"https://subsplease.org/api/?f=schedule&h=true&tz={TIMEZONE}"

        async with ClientSession() as ses:
            res = await ses.get(schedule_url)
            aniContent = json.loads(await res.text()).get("schedule")

        if not aniContent:
            logger.warning("No schedule content found.")
            return

        today_date = datetime.now(timezone(TIMEZONE))
        formatted_date = today_date.strftime("%A (%d-%m-%Y)")
        last_updated_time = today_date.strftime("%I:%M %p")

        # Calculate dynamic UTC offset
        utc_offset = today_date.utcoffset()
        offset_hours = utc_offset.total_seconds() // 3600
        offset_sign = '+' if offset_hours >= 0 else '-'
        offset_str = f"(UTC {offset_sign}{abs(int(offset_hours)):02d}:00)"

        sch_list = "\n".join(
            f"[{datetime.strptime(i['time'], '%H:%M').strftime('%I:%M %p')}] - 📌 **{i['title']}** {'✅' if i['aired'] else ''}\n"
            for i in aniContent
        )

        text = (f"📅 **Schedule for {formatted_date}**\n\n{sch_list}\n"
                f"🕒 __Last Updated:__ {last_updated_time} {offset_str}")

        await app.edit_message_text(chat_id=MAIN_CHANNEL, message_id=MESSAGE_ID, text=text)
        latest_caption = text
        logger.info("Schedule updated successfully!")

    except Exception as err:
        logger.error(f"Error updating schedule: {str(err)}")

async def update_image() -> None:
    """Update the image in the channel."""
    IMAGE_PATH = get_random_image()
    if IMAGE_PATH is None:
        return

    try:
        new_caption = latest_caption

        await app.edit_message_media(
            chat_id=MAIN_CHANNEL,
            message_id=MESSAGE_ID,
            media=InputMediaPhoto(IMAGE_PATH)
        )

        await app.edit_message_caption(
            chat_id=MAIN_CHANNEL,
            message_id=MESSAGE_ID,
            caption=new_caption
        )

        logger.info("Image and caption updated successfully!")

    except Exception as e:
        logger.error(f"Failed to update image: {str(e)}")

async def schedule_updates() -> None:
    """Updates the Schedule every 15 minutes."""
    scheduler = AsyncIOScheduler(timezone=timezone(TIMEZONE))
    scheduler.add_job(update_schedule, 'interval', minutes=15)
    scheduler.add_job(update_image, 'interval', hours=12)
    scheduler.start()

@app.on_message(filters.command('start') & filters.private)
async def start(client, message):
    """Start command handler."""
    await message.reply(
        f"💫 __Schedule is running..__"
    )

async def main() -> None:
    """Main function to run the bot."""
    logger.info("Bot started.")

    await update_image()
    await update_schedule()
    await schedule_updates()

def signal_handler(sig, frame):
    logger.info("Shutting down gracefully...")
    app.stop()
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    with app:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.run_forever()
