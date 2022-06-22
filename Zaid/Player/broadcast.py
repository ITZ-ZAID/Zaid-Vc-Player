import asyncio
import traceback

from pyrogram.types import Message
from pyrogram import filters, __version__ as pyrover
from pytgcalls import (__version__ as pytgver)

from Zaid.main import me_bot, bot as Client
from Zaid.filters import command
from Zaid.decorators import sudo_users_only
from Zaid.Database.dbchat import get_served_chats
from Zaid.Database.dbusers import get_served_users
from Zaid.Database.dbpunish import get_gbans_count

from config import BOT_USERNAME as uname


@Client.on_message(command(["broadcast", f"broadcast@{uname}"]) & ~filters.edited)
@sudo_users_only
async def broadcast_message_nopin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"✅ Broadcast complete in {sent} Group.")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n\n/broadcast (`message`) or (`reply to message`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"✅ Broadcast complete in {sent} Group.")


@Client.on_message(command(["broadcast_pin", f"broadcast_pin@{uname}"]) & ~filters.edited)
@sudo_users_only
async def broadcast_message_pin(c: Client, message: Message):
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
                m = await c.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"✅ Broadcast complete in {sent} Group.\n📌 Sent with {pin} chat pins."
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n\n/broadcast_pin (`message`) or (`reply to message`)"
        )
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
            m = await c.send_message(i, text=text)
            try:
                await m.pin(disable_notification=True)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"✅ Broadcast completed in {sent} Group.\n📌 Sent with {pin} chat pins."
    )


@Client.on_message(command(["stats", f"stats@{uname}"]) & ~filters.edited)
@sudo_users_only
async def bot_statistic(c: Client, message: Message):
    name = me_bot.first_name
    chat_id = message.chat.id
    msg = await c.send_message(
        chat_id, "❖ ꜰᴇᴀᴛᴄʜɪɴɢ ᴅᴇᴛᴀɪʟꜱ..."
    )
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    gbans_usertl = await get_gbans_count()
    tgm = f"""
📊 ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛɪᴄꜱ ᴏꜰ [{name}](https://t.me/{uname})`:`

➥ **ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ** : `{served_chats}`
➥ **ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ** : `{served_users}`
➥ **ɢʙᴀɴɴᴇᴅ ᴜꜱᴇʀꜱ** : `{gbans_usertl}`

➛ **ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** : `{pyver}`
➛ **ᴘʏ-ᴛɢᴄᴀʟʟꜱ ᴠᴇʀꜱɪᴏɴ** : `{pytgver.__version__}`
➛ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ** : `3.10.4`

🤖 ᴄᴏᴅᴇꜱ ᴠᴇʀꜱɪᴏɴ: `2.1`"""
    await msg.edit(tgm, disable_web_page_preview=True)
