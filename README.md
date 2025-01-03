[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&width=435&lines=Anime+Schedule+Bot)](https://git.io/typing-svg)

This is an Anime Schedule Telegram bot made with the Pyrogram library. The bot fetches and maintains the anime schedules from subsplease and updates a channel with the schedule along with images.

### Features
#### v2.0
- Fetches anime schedules and updates them every 15 minutes.
- Posts random images from a specified directory with schedule post.
- Each schedule post is pinned in the channel for easy access.
- Every day at 12:15 AM, the bot deletes the old schedule post and sends a new one with the latest information is available.


- Manually send the schedule (Sudo users only) by command.
- Change the TimeZone for schedule fetching (Sudo users only)  by command.
- Check Status (Current TimeZone etc..).
- Supports deployment on Koyeb.


#### v1.0
- **Functionality**: Edits the scheduled message every 15 minutes.
- **Usage**: Use [v1.0](https://github.com/CutieSoul/Anime-Schedule-Bot/tree/v1.0) if you want to edit the current scheduled message.

### Usage

- `/send` - Manually send the schedule (Sudo users only)

- `/start` - Check if bot alive

- `/status` - Get the current status of the bot

- `/set_timezone` [timezone] - Change the timezone for schedule fetching (Sudo users only)

To change the timezone, use the command followed by the desired timezone string.

Example:
```bash
/set_timezone America/New_York
```
Note: You can find valid timezone formats in the IANA time zone database.

### Requirements

- Python 3.7 or higher
- Libraries:
  - `aiohttp`
  - `pyrogram`
  - `apscheduler`
  - `pytz`
  - `python-dotenv`
  - `flask`

### Variables

* `API_ID` :
Your API ID from my.telegram.org

* `API_HASH` :
Your API HASH from my.telegram.org

* `BOT_TOKEN` :
Bot Token from @BotFather

* `MAIN_CHANNEL` :
Your Channel username (must start with @). This is where your bot will post schedule.

* `TIMEZONE` :
Your local timezone, formatted according to the IANA time zone database. For example, use America/New_York for Eastern Time.

* `SUDO_USERS` :
A comma-separated list of user IDs that have administrative privileges.

* `WEBHOOK` :
Set to `True` if you are running on Koyeb. Default is `False`.


### Installation

1. Clone the repository.
   ```bash
   sudo apt update
   sudo apt install git python3 python3-pip tmux
   git clone https://github.com/CutieSoul/Anime-Schedule-Bot && cd Anime-Schedule-Bot
   ```

2. Configure the bot by editing `.env` with your Telegram API credentials, bot token, and other settings.
   ```bash
   nano .env
   ```

3. Install Dependencies.
   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the Bot in tmux.
   ```bash
   tmux new -s schedule-bot  # Start a new tmux session named "schedule-bot"
   python3 bot.py         # Run the bot
   ```
   - To detach from the tmux session and leave the bot running, press `Ctrl + B`, then `D`.
   - To reattach to the session later, use:
     ```bash
     tmux attach -t schedule-bot
     ```

#### Deploy on Koyeb
The fastest way to deploy the application is to click the Deploy to Koyeb button below.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/CutieSoul/Anime-Schedule-Bot&env[API_ID]&env[API_HASH]&env[BOT_TOKEN]&env[WEBHOOK]=True&env[MAIN_CHANNEL]&env[TIMEZONE]&env[SUDO_USERS]&run_command=python3%20bot.py&branch=main&name=animeschedule)


### Logging

- The bot logs important actions to the console, which can help in debugging and monitoring its performance. You can adjust the logging level in the configuration if needed.
