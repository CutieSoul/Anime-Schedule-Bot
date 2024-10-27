# Do not remove credits given in this repo.
# Importing this repo instead of forking is strictly prohibited.
# Kindly fork and edit as you wish. Feel free to give credits to the developer(©️ AshinaXD).

import asyncio
import logging
from pyrogram import idle
from pyrogram.types import BotCommand
from flask import Flask
from threading import Thread
from utils.main import app, WEBHOOK
from utils.handlers import start_command, help_command, about_command
from utils.schedule import schedule_updates

logger = logging.getLogger(__name__)

# Handle button callback queries
@app.on_callback_query()
async def callback_query_handler(client, callback_query):
    """Handle button callback queries."""
    data = callback_query.data

    await callback_query.answer()

    if data == "help":
        await help_command(client, callback_query.message)
    elif data == "about":
        await about_command(client, callback_query.message)
    elif data == "start":
        await start_command(client, callback_query.message)

async def main():
    logger.info("Checking WEBHOOK condition.")
    logger.info(f"WEBHOOK value: {WEBHOOK}")
    await app.start()
    await app.set_bot_commands([
        BotCommand("start", "Check if I'm alive"),
        BotCommand("send ", "Manually send the schedule"),
        BotCommand("status ", "Get the current status"),
        BotCommand("set_timezone", " Change the timezone")])
    await schedule_updates()

    if WEBHOOK:
        logger.info("Running with Flask.")
        flask_app = Flask(__name__)

        # Start the Flask app in a separate thread
        Thread(target=flask_app.run, kwargs={'host': '0.0.0.0', 'port': 8000}).start()
    else:
        logger.info("Running without Flask.")

    logger.info("Bot started.")

    await idle()
    logger.info("Bot stopped.")
    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
