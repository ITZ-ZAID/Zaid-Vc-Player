from pyrogram import filters, Client
import asyncio
from Zaid.main import bot
from pyrogram.types import Chat, User
from typing import ClassVar, Optional
from pyrogram.types import Message
import pyrogram
from config import SUDO_USERS
from Zaid.data import REPLYRAID
from Zaid.Database.active import get_raid_chats, remove_raid_chat, add_raid_chat

from typing import List, Union
import random




NUMBER = ["0", "1"]




@bot.on_message(filters.text & ~filters.group)
async def rrl(client: bot, message: Message):
    syz = await get_raid_chats()
    for x in syz:
        queue = (await app.get_chat(x)).first_name
        if not queue:
            return
        reply = random.choice(REPLYRAID)
        caption = f"{reply}"
        await client.send_message(message.chat.id, caption)
        await asyncio.sleep(0.2)
                
@bot.on_message(filters.user(SUDO_USERS) & filters.command('replyraid'))
async def arr(client: bot, message: Message):
    if message.reply_to_message:
        a = message.reply_to_message.from_user
        b = message.reply_to_message.from_user
        e = b.id
        c = b.first_name
        chat_id = e
        username = f"[{c}](tg://user?id={e})"
        event = await message.reply_text("Reply Raid Activating....")
        que[client] = []
        await add_raid_chat(chat_id)
        await event.edit(f"Reply Raid has been activated on {username}")


@bot.on_message(filters.user(SUDO_USERS) & filters.command('dreplyraid'))
async def drr(client: bot, message: Message):
    if message.reply_to_message:
        a = message.reply_to_message.from_user
        b = message.reply_to_message
        e = b.id
        c = b.first_name
        chat_id = e
        username = f"[{c}](tg://user?id={e})"
        zaid = await message.reply_text("Reply Raid De-activating....")
        await remove_raid_chat(chat_id)
        await zaid.edit(f"Reply Raid has been De-activated on {username}")
