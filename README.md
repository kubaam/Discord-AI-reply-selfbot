# Discord AI Reply Selfbot

This project is a simple OpenAI powered selfbot that automatically replies to
messages in a chosen Discord channel. It now aims to produce more natural,
human-like responses.

> **Warning**
> Using selfbots violates the Discord [Terms of Service](https://discord.com/terms).
> This repository is provided for educational purposes only. Running the bot on
> a real account can lead to account termination.

---


## Features

- Generates short, friendly replies using GPT-4
- Word blacklist to skip certain messages
- Skips messages without real words (links or gibberish)
- Handles a single queued reply at once to avoid floods
- GUI (`config_gui.py`) to create the `config.json` file

---

## Getting Started

1. Install the dependencies (Python 3.10 or newer is recommended):
   ```bash
   pip install -r requirements.txt
   ```
2. Run the config generator and fill in your details:
   ```bash
   python config_gui.py
   ```
3. Start the selfbot:
   ```bash
   python selfbot.py
   ```

You can also provide configuration values via environment variables
(`DISCORD_TOKEN`, `GUILD_ID`, `CHANNEL_ID`, and `OPENAI_KEY`) which will take
precedence over values in `config.json`.
