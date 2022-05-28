import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Zaid.Player"},
)

BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

Test = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'Zaid.Player'})
call_py = PyTgCalls(
    Test,
    cache_duration=100,
    overload_quiet_mode=True,
)
