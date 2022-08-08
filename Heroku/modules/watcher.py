import asyncio

from pyrogram import filters, Client
from pyrogram.errors import FloodWait


from Heroku.config import SUDO_USERS
from Heroku.setup.filters import command
from Heroku.calls.calls import client as USER
from Heroku.core.chats import add_served_chat, blacklisted_chats, get_served_chats

chat_watcher_group = 10


@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(app: Client, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


@Client.on_message(command("gcast") & filters.user(SUDO_USERS))
async def broadcast_message(app: Client, message):
    if not message.reply_to_message:
        pass
    else:
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
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"**ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴍꜱɢ ɪɴ {sent}  ᴄʜᴀᴛꜱ ᴡɪᴛʜ {pin} ᴘɪɴꜱ.**"
        )
        return
    if len(message.command) < 2:
        await message.reply_text("**ᴜꜱᴀɢᴇ**:\n/gcast [ᴍᴇꜱꜱᴀɢᴇ]")
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
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"✈️ **Broadcasted message in {sent} chats and {pin} pins.**"
    )


# Broadcast without pinned


@Client.on_message(command("broadcast") & filters.user(SUDO_USERS) & ~filters.edited)
async def broadcast_message(app: Client, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage**:\n/broadcast [message]")
    sleep_time = 0.1
    text = message.text.split(None, 1)[1]
    sent = 0
    schats = await get_served_chats()
    chats = [int(chat["chat_id"]) for chat in schats]
    m = await message.reply_text(
        f"Broadcast in progress, will take {len(chats) * sleep_time} seconds."
    )
    for i in chats:
        try:
            await app.send_message(i, text=text)
            await asyncio.sleep(sleep_time)
            sent += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"✈️ **Broadcasted message in {sent} chats.**")
