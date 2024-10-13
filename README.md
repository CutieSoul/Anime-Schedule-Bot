[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&width=435&lines=Anime+Schedule+Bot)](https://git.io/typing-svg)

This is an Anime Schedule Telegram bot made with the Pyrogram library. The bot fetches and maintains the anime schedules from subsplease and updates a channel with the schedule along with images.

### Features

- Fetches anime schedules and updates them every 15 minutes.
- Posts random images from a specified directory.
- Responds to the `/start` command.
- Gracefully shuts down on receiving interrupt signals.

### Requirements

- Python 3.7 or higher
- Libraries:
  - `aiohttp`
  - `pyrogram`
  - `apscheduler`
  - `pytz`

### Variables

* `API_ID`
Your API ID from my.telegram.org

* `API_HASH`
Your API HASH from my.telegram.org

* `BOT_TOKEN`
Bot Token from @BotFather

* `MAIN_CHANNEL`
Your Channel username (must start with @). This is where your bot will post schedule.

* `MESSAGE_ID`
The ID of the initial message containing an image in your channel.

* `TIMEZONE`
Your local timezone, formatted according to the IANA time zone database. For example, use America/New_York for Eastern Time.


### Installation

1. Clone the repository
   ```bash
   sudo apt update
   sudo apt install git python3 python3-pip
   git clone https://github.com/LynomX/Anime-Schedule-Bot && cd Anime-Schedule-Bot
   ```

2. Configure the bot by editing `.env` with your Telegram API credentials, bot token, and other settings.
   ```bash
   nano .env
   ```

3. Install Dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

### Usage

4. Run the Bot
   ```bash
   python3 bot.py
   ```
### Logging

The bot logs important actions to the console, which can help in debugging and monitoring its performance. You can adjust the logging level in the configuration if needed.

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the bot.

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)

### License

This project is licensed under the MIT License

##

   **Star this Repo if you Liked it ⭐⭐⭐**
