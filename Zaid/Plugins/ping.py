from pyrogram import filters, Client
from pyrogram.types import Message
from Zaid.config import PING_IMG
from Zaid import app, SUDOERS, Music_START_TIME, BOT_USERNAME
import os
import psutil
import time
from datetime import datetime
from Zaid.MusicUtilities.helpers.time import get_readable_time

async def bot_sys_stats():
    bot_uptime = int(time.time() - Music_START_TIME)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f'''
Uptime: {get_readable_time((bot_uptime))}
CPU: {cpu}%
RAM: {mem}%
Disk: {disk}%'''
    return stats


@app.on_message(filters.command(["mping", "ping"]))
async def ping(_, message):
    uptime = await bot_sys_stats()
    start = datetime.now()
    response = await message.reply_photo(
        photo= f"{PING_IMG}",
        caption=">> Pong!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(f"**Pong!**\n`⚡{resp} ms`\n\n<b><u>📜 Music System Stats:</u></b>{uptime}")
