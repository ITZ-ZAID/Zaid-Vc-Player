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

HNDLR = '/'

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await call_py.get_chat(inp)
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



@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await call_py.get_chat(inp)
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


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await call_py.get_chat(inp)
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
