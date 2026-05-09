# ♡ Ｈḯꪀ𝚊𝖙𝚊Ｈ𝘆𝖚𝔤à ✘ ᴍᴜsɪᴄ🥀✨

A powerful Telegram music bot that allows users to play, queue, and control music in voice chats with moderation capabilities.

## Features

- 🎵 Play music from YouTube, Spotify, SoundCloud
- 📋 Queue management with shuffle and loop
- 🎚️ Volume control and audio effects
- 📝 Lyrics search
- 🎮 Fun commands (trivia, jokes, quotes)
- 🔨 Moderation tools (ban, kick, mute)
- 💬 Conversation commands with AI assistance
- 🌐 Multi-language support with personalized language selection
- 🧠 Intelligent AI-powered responses that adapt to user's language

## Setup & Installation

### Prerequisites

- Python 3.9+
- FFmpeg

### Installation

1. Clone this repository
2. Install required packages:
   ```
   pip install aiogram yt-dlp requests python-dotenv psutil
   ```
3. Create a `.env` file with your bot token:
   ```
   BOT_TOKEN=your_bot_token_here
   ```
4. Run the bot:
   ```
   python bot.py
   ```

### Bot Management

A utility script `kill_bot.py` is included to manage bot instances:

```bash
# Show help and available commands
./kill_bot.py --help

# Check bot status
./kill_bot.py status

# Stop all running bot instances
./kill_bot.py kill

# Start a new bot instance
./kill_bot.py start

# Restart the bot (stop and start)
./kill_bot.py restart

# Clean up all bot processes and lock files
./kill_bot.py clean
```

This tool helps prevent multiple bot instances from running simultaneously and causing conflicts.

## Available Commands

### Basic Commands

- `/start` - Start the bot or restart interaction
- `/help` - Show help and available commands
- `/about` - Show bot information
- `/ping` - Check if bot is online
- `/userinfo` - Get your user details

### Music Commands

- `/play <song>` - Play a song from YouTube or URL
- `/pause` - Pause current playback
- `/resume` - Resume paused playback
- `/skip` - Skip to next song
- `/stop` - Stop playback and clear queue
- `/queue` - Show current playlist
- `/nowplaying` - Show current song details
- `/loop <on/off>` - Toggle repeat mode
- `/shuffle` - Shuffle the playlist
- `/volume <1-100>` - Adjust volume
- `/add <song>` - Add song to queue without playing
- `/remove <position>` - Remove song from queue
- `/clearqueue` - Clear all songs from queue
- `/lyrics <song>` - Find song lyrics

### Voice Chat Commands

- `/joinvc` - Join voice chat
- `/leavevc` - Leave voice chat
- `/mutevc` - Mute bot in voice chat
- `/unmutevc` - Unmute bot in voice chat

### Moderation Commands

- `/ban @username` - Ban a user
- `/unban @username` - Unban a user
- `/mute @username` - Mute a user
- `/unmute @username` - Unmute a user
- `/kick @username` - Kick a user
- `/warn @username` - Give a warning to a user
- `/setwelcome <message>` - Set a custom welcome message
- `/setrules <rules>` - Set group rules

### Fun Commands

- `/photo` - Send a random photo
- `/gif` - Send a random GIF
- `/joke` - Get a random joke
- `/quote` - Get a motivational quote
- `/trivia` - Play a trivia game
- `/poll <question>` - Create a quick poll
- `/weather <city>` - Get weather updates
- `/news` - Fetch the latest news
- `/translate <text>` - Translate text to another language
- `/define <word>` - Get the dictionary meaning of a word

### Language & AI Commands

- `/languages` - Change your preferred language (supports English, Hindi, Telugu, Japanese, Chinese, Korean, Spanish, French, Russian)
- `/ai <message>` - Talk to the bot's AI in your preferred language
- You can also just chat with the bot directly without commands for natural language interaction

### Owner-Only Commands

- `/verify` - Verify bot owner identity for accessing restricted commands (Owner only)
- `/broadcast <message>` - Send a message to all users who have interacted with the bot (Owner only, requires verification)

For more details on owner commands and verification system, see [OWNER_COMMANDS.md](OWNER_COMMANDS.md).

## License

This project is licensed under the MIT License
