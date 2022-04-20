
#forked from https://github.com/The-HellBot/ArrayCore

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

from Zaid.main import call_py, bot as Zaid, Test
from config import SUDO_USERS

logging.basicConfig(level=logging.INFO)

HNDLR = '/'

aud_list = [
    "./Zaid/Audio/AUDIO1",
    "./Zaid/Audio/AUDIO2",
    "./Zaid/Audio/AUDIO3",
    "./Zaid/Audio/AUDIO4",
    "./Zaid/Audio/AUDIO5",
    "./Zaid/Audio/AUDIO6",
    "./Zaid/Audio/AUDIO7",
    "./Zaid/Audio/AUDIO8",
]



@Zaid.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    inp = e.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 

    if inp:
        Zaid = await e.reply_text("**Starting Raid**")
        link = f"https://zaid-robot.github.io/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** Ongoing Raid")


@Zaid.on_message(filters.user(SUDO_USERS) & filters.command(["vraid"], prefixes=HNDLR))
async def vraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    replied = e.reply_to_message
    inp = e.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 
    if replied:
        if replied.video or replied.document:
            suhu = await replied.reply("📥 **Downloading Your Replied File...**")
            dl = await replied.download()
    if inp:
        Zaid = await e.reply_text("**Starting Raid**")
        link = f"https://zaid-robot.github.io/{aud[1:]}"
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            await call_py.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Video:** {songname} \n**> Position:** Ongoing Raid")


@Zaid.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Test.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.leave_group_call(chat_id)
            await e.reply_text("**VC Raid Ended!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@Zaid.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Test.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.pause_stream(chat_id)
            await e.reply_text(f"**VC Raid Paued In:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@Zaid.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Test.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.resume_stream(chat_id)
            await e.reply_text(f"**VC Raid Resumed In {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No raid is currently paused!**")
