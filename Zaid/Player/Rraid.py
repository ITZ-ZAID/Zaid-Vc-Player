from pyrogram import filters, Client
import asyncio
from Zaid.main import bot
from pyrogram.types import Chat, User
from typing import ClassVar, Optional
from pyrogram.types import Message
import pyrogram
from config import SUDO_USERS
from Zaid.data import REPLYRAID

from typing import List, Union
import random




NUMBER = ["0", "1"]


que = []


@bot.on_message(filters.text & filters.private & ~filters.group)
async def rrl(client: bot, message: Message):
    global que
    queue = que.get(message.from_user.id)
    if not queue:
        return
    reply = random.choice(REPLYRAID)
    caption = f"{reply}"
    await client.send_message(message.chat.id, caption)
    await asyncio.sleep(0.2)
                
@bot.on_message(filters.user(SUDO_USERS) & filters.command('replyraid'))
async def arr(client: bot, message: Message):
    global que
    if message.reply_to_message:
        a = message.reply_to_message.from_user
        b = message.reply_to_message.from_user
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await message.reply_text("Reply Raid Activating....")
        que[client] = []
        qeue = que.get(client)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")


@bot.on_message(filters.user(SUDO_USERS) & filters.command('dreplyraid'))
async def drr(client: bot, message: Message):
    global que
    if message.reply_to_message:
        a = message.reply_to_message.from_user
        b = message.reply_to_message
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        zaid = await message.reply_text("Reply Raid De-activating....")
        queue = que.get(client)
        queue.pop(0)
        await zaid.edit(f"Reply Raid has been De-activated on {username}")
