from Music import app, SUDOERS
from pyrogram import filters, Client
from pyrogram.types import Message
import asyncio
from Music.MusicUtilities.database.chats import (get_served_chats, is_served_chat, add_served_chat, get_served_chats)
from Music.MusicUtilities.helpers.filters import command


@app.on_message(filters.command("broadcast") & filters.user(SUDOERS))
async def broadcast_message(_, message):
    if not message.reply_to_message:
        pass
    else :
        x = message.reply_to_message.message_id   
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=False)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"**Broadcasted Message In {sent}  Chats with {pin} Pins.**")  
        return
    if len(message.command) < 2:
        await message.reply_text("**Usage**:\n/broadcast [MESSAGE]")
        return  
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            try:
                await m.pin(disable_notification=False)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"**Broadcasted Message In {sent} Chats and {pin} Pins.**")
