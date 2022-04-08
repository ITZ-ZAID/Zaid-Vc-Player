import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)

from Zaid.queues import QUEUE, add_to_queue, get_queue, clear_queue

from Zaid.main import call_py, bot as vcbot
from config import SUDO_USERS

logging.basicConfig(level=logging.INFO)

HNDLR = '/'

aud_list = [
    "./Zaid/Audio/AUD1.mp3",
    "./Zaid/Audio/AUD2.mp3",
    "./Zaid/Audio/AUD3.mp3",
    "./Zaid/Audio/AUD4.mp3",
    "./Zaid/Audio/AUD5.mp3",
    "./Zaid/Audio/AUD6.mp3",
    "./Zaid/Audio/AUD7.mp3",
    "./Zaid/Audio/AUD8.mp3",
    "./Zaid/Audio/AUD9.mp3",
    "./Zaid/Audio/AUD10.mp3",
]

Venom1 = call_py

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    inp = e.text[8:]
    aud = choice(aud_list)
    chat = e.text.split(None, 2)[1]
    try:
        chat_id = (await call_py.get_chat(chat)).id
        await call_py.join_chat(chat_id)
        Zaid = await e.reply_text("**Starting VC raid**")
        link = f"https://itshellboy.tk/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat_.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
            await call_py.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat_.title} \n\n**> Audio:** {songname} \n**> Position:** Ongoing Raid")






