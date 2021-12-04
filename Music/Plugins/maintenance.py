from Music import app, SUDOERS
from pyrogram import filters, Client
from pyrogram.types import Message
from Music.MusicUtilities.database.onoff import (is_on_off, add_on, add_off)
from Music.MusicUtilities.helpers.filters import command


@Client.on_message(command("musicp") & filters.user(SUDOERS))
async def smex(_, message):
    usage = "**Usage:**\n/Musicp [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        user_id = 1
        await add_on(user_id)
        await message.reply_text("✅ Music Enabled for Maintenance")
    elif state == "disable":
        user_id = 1
        await add_off(user_id)
        await message.reply_text("❌ Maintenance Mode Disabled")
    else:
        await message.reply_text(usage)

        
@Client.on_message(command("stp") & filters.user(SUDOERS))
async def sls_skfs(_, message):
    usage = "**Usage:**\n/st [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        user_id = 2
        await add_on(user_id)
        await message.reply_text("✅ Speedtest Enabled")
    elif state == "disable":
        user_id = 2
        await add_off(user_id)
        await message.reply_text("❌ Speedtest Disabled")
    else:
        await message.reply_text(usage)
