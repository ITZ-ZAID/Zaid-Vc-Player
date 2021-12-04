from pyrogram import filters, Client
from pyrogram.types import Message
from Music import app, SUDOERS
from sys import version as pyver
import subprocess
import shutil
import os
from Music.MusicUtilities.database.functions import start_restart_stage
from Music.MusicUtilities.tgcallsrun import (music, convert, download, clear, get, is_empty, put, task_done)
from Music.MusicUtilities.database.queue import get_active_chats
from Music.MusicUtilities.database.queue import (get_active_chats, is_active_chat, add_active_chat, remove_active_chat, music_on, is_music_playing, music_off)

@app.on_message(filters.command("restart") & filters.user(SUDOERS))
async def theme_func(_, message):
    A = "downloads"
    B = "raw_files"
    shutil.rmtree(A)
    shutil.rmtree(B)
    os.mkdir(A)
    os.mkdir(B)
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        pass
    for x in served_chats:
        try:
            await app.send_message(x, "Yukki has just restarted herself. Sorry for the issues.\n\nStart playing after 10-15 seconds again.")
        except Exception:
            pass
    served_chatss = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chatss.append(int(chat["chat_id"]))
    except Exception as e:
        pass
    for served_chat in served_chatss:
        try:
            await remove_active_chat(served_chat)   
        except Exception as e:
            await message.reply_text(f"{e}")
            pass    
    x = await message.reply_text(f"__Restarting Music!__")   
    await start_restart_stage(x.chat.id, x.message_id)
    os.execvp(f"python{str(pyver.split(' ')[0])[:3]}", [
              f"python{str(pyver.split(' ')[0])[:3]}", "-m", "Music"])
