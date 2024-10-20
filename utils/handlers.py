# Do not remove credits given in this repo.
# Importing this repo instead of forking is strictly prohibited.
# Kindly fork and edit as you wish. Feel free to give credits to the developer(©️ AshinaXD).

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.main import app, SUDO_USERS, MAIN_CHANNEL
from utils.schedule import send_schedule

WELCOME_TEXT = (
    "💖 **Welcome to the Anime Schedule Bot!**\n\n"
    f"This bot is dedicated to providing updates and schedules exclusively for {MAIN_CHANNEL}. "
    "Stay tuned for the latest anime info, and enjoy the anime experience!\n\n"
    "👉 **Use the buttons below to navigate:**"
)

@app.on_message(filters.command('start') & filters.private)
async def start(client, message):
    """Start command handler."""

    # Specify the correct path to your image
    photo = 'images/msg.jpg'

    # Send the welcome image
    await client.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=WELCOME_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Help", callback_data="help"),
                InlineKeyboardButton("About", callback_data="about")
            ]
        ])
    )

async def start_command(client, message):
    """Start command handler."""
    keyboard = [
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ]
    ]
    await message.edit(WELCOME_TEXT, reply_markup=InlineKeyboardMarkup(keyboard))


# Define the help command
async def help_command(client, message):
    """Help command handler."""
    help_text = (
        "📜 **Available Commands:**\n\n"
        "1. /send - Manually send the schedule (Sudo users only) 🔒\n"
        "2. /start - Check if I'm alive 🚀\n"
        "3. /status - Get the current status of the bot 📊\n"
        "4. /set_timezone [timezone] - Change the timezone for schedule fetching 🌍 (Sudo users only) 🔒\n\n"
        "❓ **Need to find a timezone?** Click the button below:\n\n"
    )

    keyboard = [
        [InlineKeyboardButton("🌍 List of Time Zones", url="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")],
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Back", callback_data="start")
        ]
    ]

    await message.edit(help_text, reply_markup=InlineKeyboardMarkup(keyboard))

# Define the about command
async def about_command(client, message):
    """About command handler."""
    about_text = (
        "🔍 **About This Bot:**\n\n"
        "This bot fetches and maintains the anime schedules from subsplease and updates a channel with the schedule along with images.\n\n"
        "🌀 Created by [Ashina](t.me/peaceful_wolf)!\n\n"
        "✨ **Feel free to reach out if you need assistance!**"
    )

    keyboard = [
        [
            InlineKeyboardButton("Source Code", url="https://github.com/AshinaXD/Anime-Schedule-Bot"),
            InlineKeyboardButton("Back", callback_data="start")
        ]
    ]

    await message.edit(about_text, reply_markup=InlineKeyboardMarkup(keyboard))

# Define the send command
@app.on_message(filters.command('send') & filters.private)
async def post_schedule(client, message):
    """Manually trigger the schedule posting for testing, restricted to sudo users."""
    if message.from_user.id not in SUDO_USERS:
        await message.reply("🚫 **Access Denied:** You don't have permission to use this command.")
        return

    schmsg = await message.reply("Please wait... ⏳")
    try:
        await send_schedule()
        await app.edit_message_text(chat_id=message.chat.id, message_id=schmsg.id, text=f"✅ Successfully schedule post sent to {MAIN_CHANNEL}!")
    except Exception as e:
        await app.edit_message_text(chat_id=message.chat.id, message_id=schmsg.id, text=f"❌ **Error:** {str(e)}")
