# © SUPERIOR_BOTS
import io
from os import path
from typing import Callable
from asyncio.queues import QueueEmpty
import os
import random
import re
from random import choice
import aiofiles
import aiohttp
from Zaid.converter import convert
from Process.design.thumbnail import *
import ffmpeg
import requests
from Zaid.fonts import CHAT_TITLE
from PIL import Image, ImageDraw, ImageFont
from config import ASSISTANT_NAME, BOT_USERNAME, QUE_IMG, CMD_IMG, PLAY_IMG, UPDATES_CHANNEL, GROUP_SUPPORT
from Zaid.filters import command, other_filters
from Zaid.queues import QUEUE, add_to_queue
from Zaid.main import call_py, Test as user, call_py2, call_py3, call_py4, call_py5
from Zaid.utils import bash
from Zaid.main import bot as Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch
from Zaid.Database.clientdb import * 
from Zaid.Client.assistant import get_assistant_details, random_assistant
from Zaid.Client.Joiner import AssistantAdd
from Zaid.Database.active import *
from Zaid.Database.dbchat import add_served_chat, is_served_chat

import yt_dlp
import yt_dlp

ZAID_IMGS = [
    "Process/ImageFont/LightGreen.png",
    "Process/ImageFont/Red.png",
    "Process/ImageFont/Black.png",
    "Process/ImageFont/Blue.png",
    "Process/ImageFont/Grey.png",
    "Process/ImageFont/Green.png",
    "Process/ImageFont/Lightblue.png",
    "Process/ImageFont/Lightred.png",
    "Process/ImageFont/Purple.png",
    "Process/ImageFont/foreground.png",
]



def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


async def ytdl(format: str, link: str):
    stdout, stderr = await bash(f'yt-dlp --geo-bypass -g -f "[height<=?720][width<=?1280]" {link}')
    if stdout:
        return 1, stdout
    return 0, stderr

chat_id = None
DISABLED_GROUPS = []
useer = "NaN"
ACTV_CALLS = []




def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", 
        format="s16le", 
        acodec="pcm_s16le", 
        ac=2, 
        ar="48k"
    ).overwrite_output().run()
    os.remove(filename)

def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))



def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def generate_cover(thumbnail, title, userid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"thumb{userid}.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open(f"thumb{userid}.png")
    images = choice(ZAID_IMGS)
    image2 = Image.open(images)
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(f"temp{userid}.png")
    img = Image.open(f"temp{userid}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Process/ImageFont/finalfont.ttf", 60)
    font2 = ImageFont.truetype("Process/ImageFont/finalfont.ttf", 70)     
    draw.text((20, 45), f"{title[:30]}...", fill= "white", stroke_width = 1, stroke_fill="white", font=font2)
    draw.text((120, 595), f"PlAYING ON: {ctitle[:20]}...", fill="white", stroke_width = 1, stroke_fill="white" ,font=font)
    img.save(f"final{userid}.png")
    os.remove(f"temp{userid}.png")
    os.remove(f"thumb{userid}.png") 
    final = f"final{userid}.png"
    return final



    
@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
@AssistantAdd
async def play(c: Client, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    keyboard = InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("▢", callback_data="cbstop"),
                      InlineKeyboardButton("II", callback_data="cbpause"),
                      InlineKeyboardButton("‣‣", "skip"),
                      InlineKeyboardButton("▷", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/{GROUP_SUPPORT}"),
                      InlineKeyboardButton(text="• ᴜᴘᴅᴀᴛᴇ •", url=f"https://t.me/{UPDATES_CHANNEL}"),
                  ],[
                      InlineKeyboardButton("» ᴄʟᴏsᴇ «", callback_data="cls")],
                  ]
             )
    if m.sender_chat:
        return await m.reply_text("you're an __Anonymous__ Admin !\n\n» revert back to user account from admin rights.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 To use me, I need to be an **Administrator** with the following **permissions**:\n\n» ❌ __Delete messages__\n» ❌ __Add users__\n» ❌ __Manage video chat__\n\nData is **updated** automatically after you **promote me**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "missing required permission:" + "\n\n» ❌ __Manage video chat__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "missing required permission:" + "\n\n» ❌ __Delete messages__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("missing required permission:" + "\n\n» ❌ __Add users__")
        return
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **downloading audio...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{QUE_IMG}",
                    caption=f"⚡ **ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ »** `{pos}`\n\n💕 **ɴᴀᴍᴇ:** [{songname}]({link}) | `ᴍᴜsɪᴄ`\n👀 **ᴄʜᴀᴛ:** `{chat_id}`\n😌 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
            else:
             try:
                if int(assistant) == 1:
                   await call_py.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                if int(assistant) == 2:
                   await call_py2.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                if int(assistant) == 3:
                   await call_py3.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                if int(assistant) == 4:
                   await call_py4.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                if int(assistant) == 5:
                   await call_py5.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                await add_active_chat(chat_id)
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{PLAY_IMG}",
                    caption=f"💕 **ɴᴀᴍᴇ:** [{songname}]({link})\n👀 **ᴄʜᴀᴛ:** `{chat_id}`\n💫 **sᴛᴀᴜᴛs:** `ᴘʟᴀʏɪɴɢ`\n😌 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}\n📹 **sᴛʀᴇᴀᴍ ᴛʏᴘᴇ:** `ᴍᴜsɪᴄ`",
                    reply_markup=keyboard,
                )
             except Exception as e:
                await suhu.delete()
                await m.reply_text(f"🚫 ᴇʀʀᴏʀ ʙᴀʙʏ:\n\n» {e}")
        
    else:
        if len(m.command) < 2:
         await m.reply_photo(
                     photo=f"{CMD_IMG}",
                    caption="🤧**ᴜsᴀɢᴇ:/play ᴡʀɪᴛᴇ sᴏɴɢs ɴᴀᴍᴇ ᴛᴏ ᴘʟᴀʏ ʙᴀʙʏ**"
                    ,
                      reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("» ᴄʟᴏsᴇ «", callback_data="cls")
                        ]
                    ]
                )
            )
        else:
            suhu = await m.reply_text(
        f"» ᴘʀᴏᴄᴇssɪɴɢ​... ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ʙᴀʙʏ🔎"
    )
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("🥵 **ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ ʙᴀʙʏ !**")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                videoid = search[4]
                userid = m.from_user.id
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                image = await play_thumb(videoid)
                queuem = await queue_thumb(videoid)
                format = "bestaudio"
                abhi, ytlink = await ytdl(format, url)
                if abhi == 0:
                    await suhu.edit(f"💬 yt-dl issues detected\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=queuem,
                            caption=f"⚡ **ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ »** `{pos}`\n\n💕 **ɴᴀᴍᴇ:** [{songname[:22]}]({url}) | `ᴍᴜsɪᴄ`\n**⏱ ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n😌 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await suhu.edit(
                            f"**Downloader**\n\n**Title**: {title[:22]}\n\n100% ████████████100%\n\n**Time Taken**: 00:00 Seconds\n\n**Converting Audio[FFmpeg Process]**"
                        )
                            if int(assistant) == 1:
                               await call_py.join_group_call(
                                   chat_id,
                                   AudioPiped(
                                       ytlink,
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            if int(assistant) == 2:
                               await call_py2.join_group_call(
                                   chat_id,
                                   AudioPiped(
                                       ytlink,
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            if int(assistant) == 3:
                               await call_py3.join_group_call(
                                   chat_id,
                                   AudioPiped(
                                       ytlink,
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            if int(assistant) == 4:
                               await call_py4.join_group_call(
                                   chat_id,
                                   AudioPiped(
                                       ytlink,
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            if int(assistant) == 5:
                               await call_py5.join_group_call(
                                   chat_id,
                                   AudioPiped(
                                       ytlink,
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            if int(assistant) == 6:
                               await call_py.join_group_call(
                                   chat_id,
                                   AudioPiped(
                                       ytlink,
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            await add_active_chat(chat_id)
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=image,
                                caption=f"💕 **ɴᴀᴍᴇ:** [{songname[:22]}]({url})\n**⏱ ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n💫 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`\n😌 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"💬 error: `{ep}`")
